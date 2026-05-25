# DTDF Audit Data

This folder contains the raw Navarasa audit results from the empirical study described in the accompanying IEEE paper.

## Files

### cross_project_navarasa_audit.csv
Side-by-side Navarasa distribution comparison across all three projects audited in the study. This is the data behind Table 4 in the paper.

### httpie_baseline_audit.csv
Full Navarasa distribution for HTTPie CLI (github.com/httpie/cli).
- 430 tests audited across 35 test files
- Classification methodology: keyword matching against test function names with manual review for ambiguous cases
- 94% intra-rater consistency verified by author re-review of 50 tests two weeks after initial classification

### requests_baseline_audit.csv
Full Navarasa distribution for the Requests library (github.com/psf/requests).
- 345 tests audited across 9 test files
- Same keyword classification rules applied as HTTPie audit

### flask_baseline_audit.csv
Full Navarasa distribution for Flask (github.com/pallets/flask).
- 377 tests audited across 41 test files
- Same keyword classification rules applied as HTTPie audit

## Classification Rules

Tests were classified using the keyword mapping in Table 2 of the paper. The full keyword-to-dimension mapping is:

| Dimension | Keywords |
|-----------|----------|
| Shringara | basic, simple, success, ok, happy, normal, get, post, put, json, output, format, display, response, header |
| Hasya | warn, deprecat, fallback, default, graceful, soft, tolerate, ignore, compat |
| Karuna | encoding, unicode, charset, binary, empty, null, none, missing, locale, zero, blank |
| Raudra | timeout, stress, load, large, huge, slow, max, limit, many, multiple, size |
| Vira | retry, recover, resume, follow, redirect, reconnect, fallback, rebuild |
| Bhayanaka | error, fail, invalid, broken, corrupt, exception, crash, refused, unavailable |
| Bibhatsa | auth, unauthorized, forbidden, injection, malicious, credential, token, ssl, cert, secure |
| Adbhuta | boundary, edge, extreme, unusual, unexpected, special, weird, port, empty_value |
| Shanta | session, persist, config, idle, stable, state, cookie, keep, pool |

Tests with no matching keywords were assigned to Shringara as the default category.

## Replication

To replicate these audits, clone the respective repositories and apply the keyword matching rules above to all test function names in the test directories. The classification script used in this study is available in the root of this repository.
