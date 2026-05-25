"""
DTDF Navarasa Audit Script
==========================
Classifies test function names in a Python test suite across the nine
Navarasa dimensions of the Dharmik Test Design Framework (DTDF).

Usage:
    python dtdf_audit.py /path/to/tests/

Output:
    Navarasa coverage report printed to stdout
    Results saved to navarasa_audit_results.csv

Reference:
    Kumar Abhishek (2026). Dharmik Test Design: A Framework for Software
    Quality Engineering Grounded in Classical Indian Knowledge Systems.
    Software Quality Journal. https://github.com/abhi-singh-123/dtdf
"""

import os
import re
import csv
import sys
from pathlib import Path


# ── Navarasa keyword classification rules ────────────────────────────────────
NAVARASA = {
    "Shringara": [
        "basic", "simple", "success", "ok", "happy", "normal", "standard",
        "get", "post", "put", "delete", "json", "output", "format", "display",
        "response", "header", "param", "send", "request", "return", "result",
        "render", "template", "route", "view", "app", "context"
    ],
    "Hasya": [
        "warn", "deprecat", "fallback", "default", "graceful", "soft",
        "tolerate", "ignore", "compat", "legacy"
    ],
    "Karuna": [
        "encoding", "unicode", "charset", "binary", "empty", "null", "none",
        "missing", "locale", "zero", "blank"
    ],
    "Raudra": [
        "timeout", "stress", "load", "large", "huge", "slow", "max",
        "limit", "many", "multiple", "size", "big", "long"
    ],
    "Vira": [
        "retry", "recover", "resume", "follow", "redirect", "reconnect",
        "fallback", "rebuild", "restore"
    ],
    "Bhayanaka": [
        "error", "fail", "invalid", "broken", "corrupt", "exception",
        "crash", "refused", "unavailable", "raise", "except", "wrong"
    ],
    "Bibhatsa": [
        "auth", "unauthorized", "forbidden", "injection", "malicious",
        "attack", "credential", "token", "ssl", "cert", "secure", "csrf",
        "secret", "key"
    ],
    "Adbhuta": [
        "boundary", "edge", "extreme", "unusual", "unexpected", "special",
        "weird", "port", "empty_value", "special_char", "complex_url",
        "nested", "circular", "recursive"
    ],
    "Shanta": [
        "session", "persist", "config", "idle", "stable", "state",
        "cookie", "keep", "pool", "permanent", "lifetime"
    ],
}

DIMENSION_DESCRIPTIONS = {
    "Shringara": "Happy path and UX completeness",
    "Hasya":     "Graceful degradation and soft error handling",
    "Karuna":    "Accessibility and edge-user scenarios",
    "Raudra":    "Stress, load, and resource exhaustion",
    "Vira":      "Recovery, failover, and resilience",
    "Bhayanaka": "Chaos engineering and fault injection",
    "Bibhatsa":  "Security and adversarial input handling",
    "Adbhuta":   "Boundary conditions and unexpected usage",
    "Shanta":    "Long-running stability and idle behavior",
}


def classify(test_name: str) -> str:
    """Classify a test function name into a Navarasa dimension."""
    name_lower = test_name.lower()
    scores = {
        rasa: sum(1 for kw in kws if kw in name_lower)
        for rasa, kws in NAVARASA.items()
    }
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else "Shringara"


def audit_directory(test_dir: str) -> dict:
    """Run Navarasa audit on all test files in a directory."""
    counts = {r: 0 for r in NAVARASA}
    test_details = []
    total = 0

    path = Path(test_dir)
    test_files = list(path.rglob("test_*.py")) + list(path.rglob("*_test.py"))

    if not test_files:
        print(f"No test files found in {test_dir}")
        return counts, [], 0

    for test_file in sorted(test_files):
        try:
            content = test_file.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue

        for match in re.finditer(r"def (test_\w+)", content):
            name = match.group(1)
            dimension = classify(name)
            counts[dimension] += 1
            total += 1
            test_details.append({
                "test_name": name,
                "file": str(test_file.relative_to(path)),
                "dimension": dimension,
            })

    return counts, test_details, total


def print_report(counts: dict, total: int, project_name: str = ""):
    """Print a formatted Navarasa coverage report."""
    title = f"DTDF Navarasa Audit Report{' — ' + project_name if project_name else ''}"
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)
    print(f"Total tests audited: {total}")
    print()
    print(f"{'Dimension':<30} {'Count':>6} {'Percent':>8}  {'Coverage Bar'}")
    print("-" * 70)

    for rasa, count in sorted(counts.items(), key=lambda x: -x[1]):
        pct = count / total * 100 if total > 0 else 0
        bar_len = int(pct / 2)
        bar = "█" * bar_len
        flag = " ← GAP" if pct < 3.0 and rasa != "Shringara" else ""
        print(f"  {rasa:<28} {count:>6} {pct:>7.1f}%  {bar}{flag}")

    print()

    # Summary
    gaps = [r for r, c in counts.items() if c / total * 100 < 3.0 and r != "Shringara"]
    if gaps:
        print(f"Dimensions below 3% (potential gaps): {', '.join(gaps)}")
    else:
        print("No dimensions below 3% — coverage looks balanced.")

    shringara_pct = counts["Shringara"] / total * 100 if total > 0 else 0
    if shringara_pct > 60:
        print(f"\nNote: Shringara at {shringara_pct:.1f}% — happy-path concentration is high.")
        print("      Consider running a DTDF ideation session on underrepresented dimensions.")
    print()


def save_csv(counts: dict, total: int, test_details: list, output_path: str = "navarasa_audit_results.csv"):
    """Save detailed audit results to CSV."""
    with open(output_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Navarasa Dimension", "Description", "Count", "Percentage"])
        for rasa, count in sorted(counts.items(), key=lambda x: -x[1]):
            pct = count / total * 100 if total > 0 else 0
            writer.writerow([rasa, DIMENSION_DESCRIPTIONS[rasa], count, f"{pct:.1f}%"])
        writer.writerow(["Total", "", total, "100%"])

    detail_path = output_path.replace(".csv", "_detail.csv")
    with open(detail_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["test_name", "file", "dimension"])
        writer.writeheader()
        writer.writerows(test_details)

    print(f"Results saved to {output_path}")
    print(f"Detailed classifications saved to {detail_path}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python dtdf_audit.py /path/to/tests/ [project_name]")
        print("Example: python dtdf_audit.py ./tests/ HTTPie")
        sys.exit(1)

    test_dir = sys.argv[1]
    project_name = sys.argv[2] if len(sys.argv) > 2 else ""

    if not os.path.isdir(test_dir):
        print(f"Error: {test_dir} is not a directory")
        sys.exit(1)

    counts, test_details, total = audit_directory(test_dir)

    if total == 0:
        print("No test functions found.")
        sys.exit(1)

    print_report(counts, total, project_name)
    save_csv(counts, total, test_details)


if __name__ == "__main__":
    main()
