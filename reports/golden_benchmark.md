# Lab 17 Golden Set Report

- Implementation: `student`
- Kind: `golden`
- Cases: **20**
- Passed: **20/20**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **1586.5 ms**
- Average token reduction vs full source context: **6.3%**
- Golden bonus: **10/10** (100% required)

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| G01 | short_term | PASS | 0.3 | 227 | 0.0% |  |
| G02 | short_term | PASS | 0.0 | 133 | 0.0% |  |
| G08 | long_term | PASS | 2712.6 | 877 | 0.0% |  |
| G09 | long_term | PASS | 1930.9 | 1762 | 0.0% |  |
| G12 | semantic | PASS | 281.5 | 418 | 8.9% |  |
| G14 | semantic | PASS | 264.3 | 270 | 30.2% |  |
| G15 | semantic | PASS | 345.9 | 270 | 41.2% |  |
| G19 | mixed | PASS | 2485.8 | 581 | 0.0% |  |
| G03 | long_term | PASS | 1873.2 | 1771 | 0.0% |  |
| G04 | long_term | PASS | 2068.9 | 1744 | 0.0% |  |
| G05 | long_term | PASS | 2546.2 | 1780 | 0.0% |  |
| G10 | episodic | PASS | 521.1 | 292 | 0.0% |  |
| G11 | episodic | PASS | 376.3 | 296 | 0.0% |  |
| G13 | semantic | PASS | 294.6 | 416 | 26.4% |  |
| G16 | mixed | PASS | 3454.6 | 581 | 0.0% |  |
| G18 | mixed | PASS | 900.5 | 500 | 11.5% |  |
| G20 | mixed | PASS | 3354.1 | 831 | 0.0% |  |
| G06 | long_term | PASS | 2452.8 | 1732 | 0.0% |  |
| G07 | long_term | PASS | 2819.0 | 1742 | 0.0% |  |
| G17 | mixed | PASS | 3047.2 | 581 | 8.1% |  |

## Evidence excerpts

### G01 - short_term

`<SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. | assistant: Noted staging constraint. | user: Filler A about button padding. | assistant: Filler A. | user: Filler B about color tokens. | assistant: Filler B. | user: Filler C about copy tone. | assistant: Filler C. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. - user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. - assistant: Noted staging constraint. </DURA`

### G02 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### G08 - long_term

`<USER_SUMMARY> Lan Tran's primary focus is on Java and Spring Boot for the LOTUS-88 project. They do not use Python for backend development.  Lan prefers Java and Spring Boot and avoids using Python for backend development. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-17 05:30:05     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Evaluation User" }: Minh la Lan, minh dang muon them retry cho phan goi payment trong san pham cua minh va minh muon vi du code hop voi dung stack ma minh dang dung chu dung dua cho minh vi du cua ngon ngu `

### G09 - long_term

`<USER_SUMMARY> Minh's personal project is named ORCHID-27, for which Minh prefers Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project.  Minh prefers Python and dislikes Java. When explaining code, Minh prefers short examples. When discussing async/await and the confusion between coroutines and Tasks, Minh wants the explanation to use a timeline, and the assistant will prioritize using a timeline for these explanations. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS and not Python, but Minh's preference for Python still applies to personal demos like ORCHID-27. </USER_SUMMARY>`

### G12 - semantic

`EPISODE: {"id":"kb-payment-retry","entity":"Payment API Retry Policy","summary":"For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3.","source":"internal-api-guideline-v3","updated_at":"2026-08-10T00:00:00Z"} metadata= EPISODE: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. metadata= EPISODE: {"id":"kb-memory-privacy","entity":"Agent Memory Privacy Rule","summary":"Do not persist personal `

### G14 - semantic

`EPISODE: {"id":"kb-memory-privacy","entity":"Agent Memory Privacy Rule","summary":"Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL.","source":"memory-governance-policy","updated_at":"2026-08-12T00:00:00Z"} metadata= EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. metadata= EPISODE: {"id":"kb-context-budget","entity":"Memory Context Budget","summary":"Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodi`

### G15 - semantic

`EPISODE: {"id":"kb-memory-privacy","entity":"Agent Memory Privacy Rule","summary":"Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL.","source":"memory-governance-policy","updated_at":"2026-08-12T00:00:00Z"} metadata= EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. metadata= EPISODE: {"id":"kb-context-budget","entity":"Memory Context Budget","summary":"Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodi`

### G19 - mixed

`<LONG_TERM> <USER_SUMMARY> Lan Tran's primary focus is on Java and Spring Boot for the LOTUS-88 project. They do not use Python for backend development.  Lan prefers Java and Spring Boot and avoids using Python for backend development. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-17 05:31:34     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Evaluation User" }: Lan uu tien stack backend nao cho LOTUS-88?   - Created At: 2026-08-01 11:00:20     Source: message     Content: Lab Assistant (assistant): Da hieu: LOTUS-88, Java + Spring B`

### G03 - long_term

`<USER_SUMMARY> Minh's personal project is named ORCHID-27, for which Minh prefers Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project.  Minh prefers Python and dislikes Java. When explaining code, Minh prefers short examples. When discussing async/await and the confusion between coroutines and Tasks, Minh wants the explanation to use a timeline, and the assistant will prioritize using a timeline for these explanations. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS and not Python, but Minh's preference for Python still applies to personal demos like ORCHID-27. </USER_SUMMARY>`

### G04 - long_term

`<USER_SUMMARY> Minh's personal project is named ORCHID-27, for which Minh prefers Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project.  Minh prefers Python and dislikes Java. When explaining code, Minh prefers short examples. When discussing async/await and the confusion between coroutines and Tasks, Minh wants the explanation to use a timeline, and the assistant will prioritize using a timeline for these explanations. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS and not Python, but Minh's preference for Python still applies to personal demos like ORCHID-27. </USER_SUMMARY>`

### G05 - long_term

`<USER_SUMMARY> Minh's personal project is named ORCHID-27, for which Minh prefers Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project.  Minh prefers Python and dislikes Java. When explaining code, Minh prefers short examples. When discussing async/await and the confusion between coroutines and Tasks, Minh wants the explanation to use a timeline, and the assistant will prioritize using a timeline for these explanations. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS and not Python, but Minh's preference for Python still applies to personal demos like ORCHID-27. </USER_SUMMARY>`

### G10 - episodic

`EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Da ghi nhan trajectory: increase timeout khong hieu qua; ClientSession + concurrency=20 giai quyet connection churn. EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Toi se uu tien timeline khi giai thich coroutine va Task. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open l`

### G11 - episodic

`EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHID-27. EPISODE: Da ghi nhan trajectory: increase timeout khong hieu qua; ClientSession + concurrency=20 giai quyet connection churn. EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Da tach scope: `

### G13 - semantic

`EPISODE: {"id":"kb-async-http","entity":"Async HTTP Incident Playbook","summary":"When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST.","source":"incident-playbook-2026","updated_at":"2026-08-11T00:00:00Z"} metadata= EPISODE: When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST. metadata= EPISODE: {"id":"kb-memory-privacy","entity":"Agent Memory Privacy Rule","summary":"Do not persist personal data witho`

### G16 - mixed

`<LONG_TERM> <USER_SUMMARY> Minh's personal project is named ORCHID-27, for which Minh prefers Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project.  Minh prefers Python and dislikes Java. When explaining code, Minh prefers short examples. When discussing async/await and the confusion between coroutines and Tasks, Minh wants the explanation to use a timeline, and the assistant will prioritize using a timeline for these explanations. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS and not Python, but Minh's preference for Python still applies to personal demos like ORCHID-27. </U`

### G18 - mixed

`<EPISODIC> EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHID-27. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Toi se uu tien timeline khi giai thich coroutine va Task. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LA`

### G20 - mixed

`<LONG_TERM> <USER_SUMMARY> Minh's personal project is named ORCHID-27, for which Minh prefers Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project.  Minh prefers Python and dislikes Java. When explaining code, Minh prefers short examples. When discussing async/await and the confusion between coroutines and Tasks, Minh wants the explanation to use a timeline, and the assistant will prioritize using a timeline for these explanations. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS and not Python, but Minh's preference for Python still applies to personal demos like ORCHID-27. </U`

### G06 - long_term

`<USER_SUMMARY> Minh's personal project is named ORCHID-27, for which Minh prefers Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project.  Minh prefers Python and dislikes Java. When explaining code, Minh prefers short examples. When discussing async/await and the confusion between coroutines and Tasks, Minh wants the explanation to use a timeline, and the assistant will prioritize using a timeline for these explanations. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS and not Python, but Minh's preference for Python still applies to personal demos like ORCHID-27. </USER_SUMMARY>`

### G07 - long_term

`<USER_SUMMARY> Minh's personal project is named ORCHID-27, for which Minh prefers Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project.  Minh prefers Python and dislikes Java. When explaining code, Minh prefers short examples. When discussing async/await and the confusion between coroutines and Tasks, Minh wants the explanation to use a timeline, and the assistant will prioritize using a timeline for these explanations. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS and not Python, but Minh's preference for Python still applies to personal demos like ORCHID-27. </USER_SUMMARY>`

### G17 - mixed

`<LONG_TERM> <USER_SUMMARY> Minh's personal project is named ORCHID-27, for which Minh prefers Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project.  Minh prefers Python and dislikes Java. When explaining code, Minh prefers short examples. When discussing async/await and the confusion between coroutines and Tasks, Minh wants the explanation to use a timeline, and the assistant will prioritize using a timeline for these explanations. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS and not Python, but Minh's preference for Python still applies to personal demos like ORCHID-27. </U`
