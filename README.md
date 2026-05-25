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

DTDF was validated through Navarasa audits of three widely used open-source Python projects.

### Cross-Project Navarasa Distribution

| Navarasa Dimension | HTTPie (n=430) | Requests (n=345) | Flask (n=377) | Average |
|---|---|---|---|---|
| Shringara (happy path) | 60.7% | 71.9% | 72.9% | 68.5% |
| Bhayanaka (fault injection) | 5.3% | 6.4% | 8.5% | 6.7% |
| Bibhatsa (security) | 4.7% | 7.8% | 1.3% | 4.6% |
| Raudra (stress/load) | 7.2% | 2.9% | 2.7% | 4.3% |
| Shanta (steady-state) | 7.0% | 2.6% | 6.4% | 5.3% |
| Karuna (edge-user) | 5.8% | 2.9% | 2.7% | 3.8% |
| Hasya (graceful degrad.) | 4.7% | 1.4% | 2.7% | 2.9% |
| Vira (recovery) | 2.8% | 3.8% | 0.8% | 2.5% |
| Adbhuta (boundary) | 1.9% | 0.3% | 2.1% | 1.4% |

The pattern is consistent across all three projects: happy-path (Shringara) tests average 68.5% while boundary (Adbhuta) tests average just 1.4%. This skew holds across different project domains, architectures, and development teams.

### DTDF Intervention on HTTPie CLI

A single DTDF ideation session on HTTPie CLI produced 37 new tests across five underrepresented dimensions. Key finding: the Vira-guided tests uncovered a specification gap — no existing test verified that timeout failures produce a distinct exit code (`ExitStatus.ERROR_TIMEOUT`) from generic errors — leaving that behavioral contract vulnerable to undetected regression.

---

## Files in This Repository

```
dtdf/
├── README.md                          — This file
├── CHECKLIST.md                       — Printable Navarasa checklist for planning sessions
├── dtdf_audit.py                      — Run a Navarasa audit on any Python test suite
├── CITATION.cff                       — Citation file for academic use
├── LICENSE                            — MIT License
├── tests/
│   └── test_dtdf_navarasa.py          — DTDF-guided tests written for HTTPie CLI
└── audit_data/
    ├── README.md                      — Explanation of audit methodology
    ├── cross_project_navarasa_audit.csv  — All three projects side by side
    ├── httpie_baseline_audit.csv      — HTTPie CLI full audit (430 tests)
    ├── requests_baseline_audit.csv    — Requests library full audit (345 tests)
    └── flask_baseline_audit.csv       — Flask framework full audit (377 tests)
```

---

## Running the Audit Tool

Audit any Python test suite with one command:

```bash
python dtdf_audit.py /path/to/your/tests/ "Your Project Name"
```

Example output:
```
============================================================
DTDF Navarasa Audit Report — Your Project
============================================================
Total tests audited: 430

Dimension                      Count  Percent  Coverage Bar
----------------------------------------------------------------------
  Shringara                      261   60.7%  ██████████████████████████████
  Raudra                          31    7.2%  ███
  Shanta                          30    7.0%  ███
  ...
  Vira                            12    2.8%  █ ← GAP
  Adbhuta                          8    1.9%  █ ← GAP

Dimensions below 3% (potential gaps): Vira, Adbhuta
```

---

## Using the Checklist

See [CHECKLIST.md](CHECKLIST.md) for a ready-to-use planning checklist. Print it or copy it into your team wiki.

---

## Paper

This framework is described in full in the accompanying paper:

> Kumar Abhishek, "Dharmik Test Design: A Framework for Software Quality Engineering Grounded in Classical Indian Knowledge Systems," *Software Quality Journal*, Springer, 2026 (under review).

---

## License

MIT License. See [LICENSE](LICENSE).

---

## Author

Kumar Abhishek
Independent Researcher, USA
ORCID: [0009-0005-7443-0235](https://orcid.org/0009-0005-7443-0235)
