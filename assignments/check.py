#!/usr/bin/env python3
"""Minimal project check utility for this repository.

This script validates that the expected top-level project files exist and can be
used as a simple sanity check when working in the repo.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable, List


REQUIRED_FILES = (
    "README.md",
    "PROCESS.md",
)


def find_missing_files(root: str | Path) -> List[str]:
    """Return a list of required files that are missing from the project root."""
    project_root = Path(root)
    missing: List[str] = []
    for filename in REQUIRED_FILES:
        if not (project_root / filename).is_file():
            missing.append(filename)
    return missing


def check_project(root: str | Path) -> bool:
    """Return True when the repository contains the expected project files."""
    return not find_missing_files(root)


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Check whether the expected repository files are present."
    )
    parser.add_argument(
        "root",
        nargs="?",
        default=".",
        help="Project root to validate (defaults to the current directory).",
    )
    args = parser.parse_args(list(argv) if argv is not None else None)

    missing = find_missing_files(args.root)
    if not missing:
        print("Project check passed: all required files are present.")
        return 0

    print("Project check failed. Missing files:")
    for name in missing:
        print(f"- {name}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
