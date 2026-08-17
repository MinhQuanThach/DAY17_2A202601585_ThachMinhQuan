from __future__ import annotations

from typing import Any

from .config import settings
from .context_budget import ContextBudgetManager
from .utils import cap_query, join_nonempty
from .zep_common import prime_eval_thread, render_graph_search

# How many characters of each episode we keep when rendering user episodic hits.
# The marker-bearing message in this dataset ("... concurrency=20 ... ASYNC-FIX-20")
# is ~165 chars, so 200 never truncates a marker, yet still lets ~4-5 distinct
# episodes fit inside the 3% episodic budget instead of one verbose transcript.
EPISODE_CHAR_CAP = 200

# The Context Block is relevance-ranked and fairly short. A separate edge (fact)
# search is what actually surfaces low-salience durable facts such as the
# open-loop deadline; a small limit tends to drop them, hence 24.
FACT_SEARCH_LIMIT = 24


class StudentMemory:
    """Only this file needs to be edited by students."""

    def __init__(self, client: Any):
        self.client = client
        self.budget = ContextBudgetManager(settings.context_tokens)

    # NOTE: Zep rejects graph.search queries longer than 400 characters. Some
    # eval queries are longer than that, so wrap every query with
    # `cap_query(query)` (see src/utils.py) before passing it to graph.search.

    def retrieve_long_term(self, user_id: str, thread_id: str, query: str) -> str:
        """Cross-session declarative memory = Zep Context Block + user facts.

        Everything here is scoped by `user_id` / a thread that belongs to that
        user, which is what keeps Minh's memory out of Lan's answer (E09).
        """
        # The Context Block is computed *relative to the current thread*, so the
        # evaluation thread must first contain the query. `ignore_roles=["user"]`
        # inside this helper means the probe message steers retrieval without
        # being written back into the user graph as a new durable fact.
        prime_eval_thread(self.client, user_id, thread_id, query)

        user_context = self.client.thread.get_user_context(thread_id=thread_id)
        context_block = getattr(user_context, "context", "") or ""

        # Second pass over the user graph edges. Edges are the extracted facts,
        # and each carries valid_at / invalid_at, so a superseded preference
        # stays visible next to the current one (recency/conflict, E08).
        try:
            edges = self.client.graph.search(
                user_id=user_id,
                query=cap_query(query),
                scope="edges",
                limit=FACT_SEARCH_LIMIT,
            )
            fact_text = render_graph_search(edges)
        except Exception:
            # A failed fact search must not lose the Context Block we already have.
            fact_text = ""

        return join_nonempty([context_block, fact_text], sep="\n\n")

    def retrieve_episodic(self, user_id: str, query: str) -> str:
        """Past trajectories of THIS user: what was tried, what worked, why.

        `scope="episodes"` returns the raw ingested source instead of extracted
        facts, which is what preserves the verbatim trajectory and its incident
        marker (E04) and the reflection wording (E05).
        """
        results = self.client.graph.search(
            user_id=user_id,
            query=cap_query(query),
            scope="episodes",
            limit=15,
        )
        return render_graph_search(results, episode_char_cap=EPISODE_CHAR_CAP)

    def retrieve_semantic(self, graph_id: str, query: str) -> str:
        """Shared domain knowledge from the standalone graph.

        `graph_id`, never `user_id`: this KB belongs to no one user. Scope is
        "episodes" because the raw documents keep the literal markers
        (PAYMENT-RULE-3, CONN-POOL-FIRST); "auto" would return extracted facts
        that paraphrase the rule and drop those codes.
        """
        capped = cap_query(query)
        try:
            results = self.client.graph.search(
                graph_id=graph_id,
                query=capped,
                scope="episodes",
                limit=8,
            )
        except Exception:
            # Some accounts/SDK versions do not expose the episodes scope on a
            # standalone graph; entity nodes still carry the marker in summary.
            results = self.client.graph.search(
                graph_id=graph_id,
                query=capped,
                scope="nodes",
                limit=8,
            )
        return render_graph_search(results)

    def assemble_context(self, layers: dict[str, str]) -> tuple[str, dict[str, dict[str, int]]]:
        """Merge the layers under the 10/4/3/3 budget, short-term first.

        Retrieval quality is not the only failure mode: an unbounded merge
        floods the prompt. `ContextBudgetManager.assemble` walks the priority
        order (short_term -> long_term -> episodic -> semantic), trims each
        layer to its own share of the context window and reports the per-layer
        token accounting used in the benchmark report.
        """
        return self.budget.assemble(layers)
