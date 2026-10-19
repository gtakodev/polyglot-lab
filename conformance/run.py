#!/usr/bin/env python3
"""Conformance runner — black-box tests shared by every language.

It only knows the CLI contract from SPEC.md: a command, arguments, a working
directory, an exit code and one JSON object on stdout. It never imports your
code, so the same suite judges Java, Kotlin, Go, Rust and TypeScript.

Usage:
    python3 conformance/run.py --cmd "go run ."                 # all cases
    python3 conformance/run.py --cmd "cargo run --quiet --" --upto M1
    python3 conformance/run.py --cmd "npx tsx src/main.ts" --only 07-retries -v

Exit code: 0 when every selected case passes, 1 otherwise.
"""

from __future__ import annotations

import argparse
import json
import shlex
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

CASES_DIR = Path(__file__).resolve().parent / "cases"
MILESTONES = ["M0", "M1", "M2", "M3"]
PER_CASE_TIMEOUT_S = 120


def absolutize(cmd: list[str], base: Path) -> list[str]:
    """Turn relative path arguments into absolute ones.

    Cases run inside a temporary directory, so a command like
    ``node dist/main.js`` or ``java -cp target/classes Main`` would otherwise
    point at the wrong place. Paths are resolved against the directory the
    runner was invoked from.
    """
    resolved: list[str] = []
    for token in cmd:
        if token.startswith("-"):
            resolved.append(token)
            continue
        if token == "." or ("/" in token and not token.startswith("/")):
            candidate = (base / token).resolve()
            if candidate.exists():
                resolved.append(str(candidate))
                continue
        resolved.append(token)
    return resolved


def load_case(case_dir: Path) -> dict:
    meta_path = case_dir / "case.json"
    if not meta_path.is_file():
        raise SystemExit(f"missing {meta_path}")
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    meta.setdefault("args", [])
    meta.setdefault("milestone", "M3")
    return meta


def run_case(cmd: list[str], case_dir: Path, meta: dict):
    with tempfile.TemporaryDirectory(prefix="tasklite-") as tmp:
        work = Path(tmp)
        for item in case_dir.iterdir():
            if item.name == "case.json":
                continue
            if item.is_dir():
                shutil.copytree(item, work / item.name)
            else:
                shutil.copy2(item, work / item.name)

        started = time.monotonic()
        try:
            proc = subprocess.run(
                cmd + meta["args"],
                cwd=work,
                capture_output=True,
                text=True,
                timeout=PER_CASE_TIMEOUT_S,
            )
        except FileNotFoundError as exc:
            return {"error": f"command not found: {exc}", "duration_ms": 0}
        except subprocess.TimeoutExpired:
            return {"error": f"runner timeout after {PER_CASE_TIMEOUT_S}s", "duration_ms": 0}
        elapsed_ms = (time.monotonic() - started) * 1000
        return {
            "exit_code": proc.returncode,
            "stdout": proc.stdout,
            "stderr": proc.stderr,
            "duration_ms": elapsed_ms,
        }


def parse_report(stdout: str):
    """Return (report_or_None, error_message)."""
    text = stdout.strip()
    if not text:
        return None, "stdout is empty (expected one JSON object)"
    try:
        return json.loads(text), None
    except json.JSONDecodeError:
        # Tolerate leading log lines only if the JSON is the last line.
        last = text.splitlines()[-1]
        try:
            return json.loads(last), None
        except json.JSONDecodeError:
            return None, "stdout is not valid JSON"


def compare(meta: dict, outcome: dict) -> list[str]:
    """Return a list of human-readable failures (empty = pass)."""
    if "error" in outcome:
        return [outcome["error"]]

    expected = meta.get("expect", {})
    failures: list[str] = []

    want_exit = expected.get("exit_code")
    if want_exit is not None and outcome["exit_code"] != want_exit:
        failures.append(f"exit code: expected {want_exit}, got {outcome['exit_code']}")

    max_ms = expected.get("max_duration_ms")
    if max_ms is not None and outcome["duration_ms"] > max_ms:
        failures.append(
            f"wall time: expected <= {max_ms} ms, got {outcome['duration_ms']:.0f} ms "
            "(concurrency not effective?)"
        )

    report, err = parse_report(outcome["stdout"])
    if report is None:
        failures.append(f"{err}; stderr: {outcome['stderr'].strip()[:400]}")
        return failures

    want_status = expected.get("status")
    if want_status is not None and report.get("status") != want_status:
        failures.append(f"status: expected {want_status!r}, got {report.get('status')!r}")

    want_codes = expected.get("error_codes")
    if want_codes is not None:
        got = sorted({e.get("code") for e in report.get("errors", []) if isinstance(e, dict)})
        if sorted(set(want_codes)) != got:
            failures.append(f"error codes: expected {sorted(set(want_codes))}, got {got}")

    want_tasks = expected.get("tasks")
    if want_tasks is not None:
        got_tasks = {}
        for task in report.get("tasks", []):
            if isinstance(task, dict) and "id" in task:
                got_tasks[task["id"]] = task
        for task_id, fields in want_tasks.items():
            actual = got_tasks.get(task_id)
            if actual is None:
                failures.append(f"task {task_id!r}: missing from report")
                continue
            for field, want_value in fields.items():
                got_value = actual.get(field, "<absent>")
                if got_value != want_value:
                    failures.append(
                        f"task {task_id!r}.{field}: expected {want_value!r}, got {got_value!r}"
                    )
        if expected.get("exact_tasks", True):
            extra = set(got_tasks) - set(want_tasks)
            if extra:
                failures.append(f"unexpected tasks in report: {sorted(extra)}")

    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description="tasklite conformance suite")
    parser.add_argument("--cmd", default=None, help='command that launches the built binary, e.g. "./tasklite"')
    parser.add_argument("--upto", choices=MILESTONES, default="M3", help="run cases up to this milestone")
    parser.add_argument("--only", action="append", default=[], help="run only these case names (repeatable)")
    parser.add_argument("--list", action="store_true", help="list cases and exit")
    parser.add_argument("-v", "--verbose", action="store_true", help="show stdout/stderr on failure")
    args = parser.parse_args()

    if not args.list and not args.cmd:
        parser.error("--cmd is required unless --list is used")
    cmd = absolutize(shlex.split(args.cmd), Path.cwd()) if args.cmd else []
    case_dirs = sorted(d for d in CASES_DIR.iterdir() if d.is_dir())
    selected = []
    for case_dir in case_dirs:
        meta = load_case(case_dir)
        if args.only and case_dir.name not in args.only:
            continue
        if MILESTONES.index(meta["milestone"]) > MILESTONES.index(args.upto):
            continue
        selected.append((case_dir, meta))

    if args.list or not selected:
        for case_dir, meta in selected or [(d, load_case(d)) for d in case_dirs]:
            print(f"{case_dir.name:24} {meta['milestone']:3} {meta.get('title', '')}")
        return 0

    print(f"tasklite conformance — {len(selected)} case(s), command: {' '.join(cmd)}\n")
    failures_total = 0
    for case_dir, meta in selected:
        outcome = run_case(cmd, case_dir, meta)
        failures = compare(meta, outcome)
        label = "PASS" if not failures else "FAIL"
        print(f"[{label}] {case_dir.name:24} {meta.get('title', '')}")
        if failures:
            failures_total += 1
            for line in failures:
                print(f"       - {line}")
            if args.verbose:
                if "stdout" in outcome and outcome["stdout"].strip():
                    print("       stdout:")
                    for line in outcome["stdout"].rstrip().splitlines():
                        print(f"         {line}")
                if "stderr" in outcome and outcome["stderr"].strip():
                    print("       stderr:")
                    for line in outcome["stderr"].rstrip().splitlines():
                        print(f"         {line}")

    total = len(selected)
    print(f"\n{total - failures_total}/{total} case(s) passed.")
    return 0 if failures_total == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
