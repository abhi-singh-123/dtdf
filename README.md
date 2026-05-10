# Dharmik Test Design Framework (DTDF)

A structured framework for software test scenario ideation, grounded in Vedic philosophy and Indian mythological archetypes.

---

## The Problem DTDF Solves

Most test suites default to testing the happy path. Code coverage looks fine. Regression runs pass. And then a production incident exposes an entire category of behavior nobody thought to test.

DTDF gives you a complete vocabulary for thinking through what to test — not just how to run tests once you have them.

---

## The Four Pillars

### 1. Navarasa Test Dimensions

Map the nine emotional essences of the Navarasas (from Bharata Muni's Natyashastra, ~2nd century BCE) to nine test design dimensions:

| Rasa | Meaning | Test Dimension |
|------|---------|----------------|
| Shringara | Love, delight | Happy path and UX completeness |
| Hasya | Humor, lightness | Graceful degradation and soft errors |
| Karuna | Compassion, sorrow | Accessibility and edge-user scenarios |
| Raudra | Fury, intensity | Stress, load, resource exhaustion |
| Vira | Heroism, courage | Recovery, failover, resilience |
| Bhayanaka | Fear, dread | Chaos engineering, fault injection |
| Bibhatsa | Disgust, aversion | Security and adversarial inputs |
| Adbhuta | Wonder, surprise | Boundary conditions, unusual inputs |
| Shanta | Peace, stillness | Long-running stability, idle behavior |

**How to use it:** Before writing tests for any feature, scan through all nine dimensions and ask: have we designed test cases for each one? Which dimensions are missing?

### 2. Panchatantra Combinatorial Model (PCM)

From the Panchatantra (attributed to Vishnu Sharma, ~300 BCE), a decision-tree approach to path-dependent test coverage. Models a system as a tree where each level represents an action or event, and each leaf represents an outcome requiring a test assertion. Particularly useful for finding bugs that only appear in specific sequences of operations.

### 3. Dharma-Adharma Oracle Model

Organizes test assertions into three types:

- **Dharmic oracles** — properties that must hold in all contexts (system invariants, safety properties)
- **Contextual oracles** — properties that must hold for specific roles or states (role-based behavior)
- **Adharmic detectors** — properties that must never hold regardless of context (security boundaries, forbidden states)

### 4. Trimurti Lifecycle Model

Diagnoses how testing effort is distributed across the test lifecycle:

- **Brahma (Creation)** — writing new tests, test data, environment setup
- **Vishnu (Preservation)** — maintaining tests, fixing flakiness, monitoring regressions
- **Shiva (Transformation)** — pruning obsolete tests, refactoring test infrastructure

---

## Empirical Validation

DTDF was validated on [HTTPie CLI](https://github.com/httpie/cli), a widely used open-source HTTP client.

**Baseline audit of 430 existing tests:**

| Dimension | Tests | Coverage |
|-----------|-------|----------|
| Shringara | 261 | 60.7% |
| Raudra | 31 | 7.2% |
| Shanta | 30 | 7.0% |
| Karuna | 25 | 5.8% |
| Bhayanaka | 23 | 5.3% |
| Hasya | 20 | 4.7% |
| Bibhatsa | 20 | 4.7% |
| Vira | 12 | 2.8% |
| Adbhuta | 8 | 1.9% |

**DTDF ideation results:** A single session targeting authentication, error handling, and CLI parsing produced 37 new tests across five underrepresented dimensions. The Vira-guided tests uncovered a specification gap: no existing test verified that timeout failures produce a distinct exit code (`ExitStatus.ERROR_TIMEOUT`) from generic errors, leaving that behavioral contract vulnerable to undetected regression.

---

## Files in This Repository

```
dtdf/
├── README.md              — This file
├── CHECKLIST.md           — Printable Navarasa checklist for planning sessions
├── CITATION.cff           — Citation file for academic use
├── LICENSE                — MIT License
└── tests/
    └── test_dtdf_navarasa.py  — DTDF-guided tests written for HTTPie CLI validation
```

---

## Using the Checklist

See [CHECKLIST.md](CHECKLIST.md) for a ready-to-use planning checklist. Print it or copy it into your team wiki.

---

## Paper

This framework is described in full in the accompanying IEEE Access paper:

> Kumar Abhishek, "Dharmik Test Design: A Framework for Software Quality Engineering Inspired by Vedic and Indian Mythological Archetypes," *IEEE Access*, 2025.

---

## License

MIT License. See [LICENSE](LICENSE).

---

## Author

Kumar Abhishek  
Independent Researcher  
ORCID: [0009-0005-7443-0235](https://orcid.org/0009-0005-7443-0235)  
