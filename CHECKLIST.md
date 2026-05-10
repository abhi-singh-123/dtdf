# DTDF Navarasa Test Design Checklist

Use this checklist at the start of test planning for any feature or system.
For each dimension, ask: have we designed test cases here? Would we detect a bug here?

---

## How to Run a DTDF Session

1. Pick a specific subsystem or feature to audit
2. Go through each dimension below in order
3. For each one, write down at least two test scenario candidates before moving on
4. Flag any dimension where the team struggles to generate scenarios — that is your biggest gap

---

## The Nine Dimensions

### 1. Shringara — Happy Path and UX Completeness
*The system working exactly as intended for its primary users*

- [ ] Core user flows succeed end to end
- [ ] Expected outputs match specifications exactly
- [ ] Successful state transitions produce correct results
- [ ] Default configurations work without modification

**Ask yourself:** If a new user followed the documentation exactly, would every step work?

---

### 2. Hasya — Graceful Degradation and Soft Errors
*The system staying usable when something minor goes wrong*

- [ ] Non-fatal warnings are surfaced without crashing
- [ ] Deprecated features still work or give clear migration guidance
- [ ] Partial failures degrade gracefully rather than failing completely
- [ ] Default fallbacks activate correctly when optional components are missing

**Ask yourself:** What happens when the system encounters something unexpected but recoverable?

---

### 3. Karuna — Accessibility and Edge-User Scenarios
*Users who operate outside the assumed happy-path context*

- [ ] Non-ASCII input is handled correctly
- [ ] Users with low bandwidth or slow connections are not left hanging
- [ ] Empty, null, or missing inputs produce clear error messages
- [ ] Edge-case user configurations (unusual locales, restricted environments) work

**Ask yourself:** Who is the most different from our assumed user, and does the system work for them?

---

### 4. Raudra — Stress, Load, and Resource Exhaustion
*The system under intense pressure*

- [ ] Performance degrades gracefully at high load rather than failing hard
- [ ] Resource limits (memory, file handles, connections) are respected
- [ ] Large inputs are handled without timeout or crash
- [ ] Concurrent requests do not produce race conditions

**Ask yourself:** What happens when ten times the expected traffic arrives at once?

---

### 5. Vira — Recovery, Failover, and Resilience
*The system bouncing back from adversity*

- [ ] Retry logic activates correctly after transient failures
- [ ] Failover to backup systems completes within expected time
- [ ] Error exit codes are distinct and documented (e.g. timeout vs generic error)
- [ ] Recovery from partial writes or interrupted operations leaves consistent state

**Ask yourself:** After every type of failure, does the system recover cleanly and signal what happened?

---

### 6. Bhayanaka — Chaos and Fault Injection
*Deliberately breaking things to see what happens*

- [ ] Random component failures do not cause cascading outages
- [ ] Network latency injection does not produce silent failures
- [ ] Disk or memory exhaustion produces clear errors not silent data corruption
- [ ] Killing processes mid-operation leaves the system in a recoverable state

**Ask yourself:** If we randomly kill a dependency right now, what is the user experience?

---

### 7. Bibhatsa — Security and Adversarial Inputs
*Users or systems trying to make the system do something it should not*

- [ ] SQL, command, and header injection attempts are rejected safely
- [ ] Credentials are never logged or leaked in error output
- [ ] Authentication cannot be bypassed through malformed inputs
- [ ] Rate limiting and access controls hold under adversarial conditions

**Ask yourself:** What is the worst thing a malicious user could do with this interface?

---

### 8. Adbhuta — Boundary Conditions and Unexpected Usage
*The edges of what the system accepts*

- [ ] Maximum and minimum valid input values are handled correctly
- [ ] Empty inputs, zero values, and single-element collections behave correctly
- [ ] Unusual but valid combinations of parameters work as expected
- [ ] Inputs at exact boundaries (e.g. port 65535, max string length) are tested

**Ask yourself:** What are the most unusual inputs that are technically valid?

---

### 9. Shanta — Long-Running Stability and Idle Behavior
*The system running quietly over a long period*

- [ ] Memory usage remains stable over extended operation (no leaks)
- [ ] Sessions and tokens expire and renew correctly over time
- [ ] Idle connections time out and reconnect cleanly
- [ ] Scheduled jobs complete reliably over days and weeks

**Ask yourself:** What would we only notice if we left the system running for a week?

---

## Scoring Your Test Suite

After auditing your existing tests against these dimensions, calculate your DTDF coverage:

```
Dimension Coverage = (Tests in dimension / Total tests) x 100
```

A healthy distribution has no dimension below 5%. Any dimension below 2% is a priority gap.

---

## Tips for the Ideation Session

- **Time-box each dimension** to 10 minutes. Do not spend 40 minutes on Shringara and skip Bhayanaka.
- **Write scenarios in plain language first.** Do not start coding until you have listed everything you want to test.
- **The dimensions you find hardest to fill are your real gaps.** If the team cannot think of Karuna scenarios, that is the problem, not the solution.
- **One person should own the checklist** and move the group from dimension to dimension.
- **Revisit quarterly.** New features create new gaps in dimensions you previously covered.
