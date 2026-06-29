#!/usr/bin/env python3
"""
Scaffold a new LeetCode problem directory.

Usage:
    python scripts/create_solution_folder.py <id> <difficulty> <slug>

Example:
    python scripts/create_solution_folder.py 42 hard trapping-rain-water
"""

import argparse
import sys
from pathlib import Path

DIFFICULTIES = {"easy", "medium", "hard"}
REPO_ROOT = Path(__file__).resolve().parent.parent


def create_solution_folder(problem_id: int, difficulty: str, slug: str) -> None:
    slug = slug.lower().replace(" ", "-")
    folder_name = f"{problem_id}-{slug}"
    folder_path = REPO_ROOT / difficulty / folder_name

    if folder_path.exists():
        sys.exit(f"Error: {folder_path} already exists.")

    folder_path.mkdir(parents=True)

    title = slug.replace("-", " ").title()
    test_name = slug.replace("-", "_")

    (folder_path / "solution.py").write_text(
        f'"""\n'
        f"{problem_id}. {title}\n"
        f"Difficulty: {difficulty.capitalize()}\n"
        f"\n"
        f"Approach:\n"
        f"-\n"
        f"\n"
        f"Time Complexity: O(?)\n"
        f"Space Complexity: O(?)\n"
        f'"""\n'
        f"\n"
        f"from typing import List\n"
        f"\n"
        f"\n"
        f"class Solution:\n"
        f"    pass  # TODO: implement\n",
        encoding="utf-8",
    )

    (folder_path / f"test_{test_name}.py").write_text(
        "from solution import Solution\n"
        "\n"
        "\n"
        "def test_example_1():\n"
        "    pass  # TODO: add test cases\n",
        encoding="utf-8",
    )

    (folder_path / "README.md").write_text(
        f"# {problem_id}. {title}\n"
        f"\n"
        f"## Problem\n"
        f"\n"
        f"**Problem description goes here.**\n"
        f"\n"
        f"---\n"
        f"\n"
        f"## Approach\n"
        f"\n"
        f"-\n"
        f"\n"
        f"---\n"
        f"\n"
        f"## Complexity\n"
        f"\n"
        f"- Time Complexity: `O(?)`\n"
        f"- Space Complexity: `O(?)`\n"
        f"\n"
        f"---\n"
        f"\n"
        f"## Solution\n"
        f"\n"
        f"[solution.py](./solution.py)\n",
        encoding="utf-8",
    )

    print(f"Created: {folder_path}/")
    print(f"  solution.py, test_{test_name}.py, README.md")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Scaffold a new LeetCode problem directory.",
        epilog="Example: python scripts/create_solution_folder.py 42 hard trapping-rain-water",  # noqa: E501
    )
    parser.add_argument("id", type=int, help="LeetCode problem ID")
    parser.add_argument(
        "difficulty", choices=sorted(DIFFICULTIES), help="Problem difficulty"
    )
    parser.add_argument(
        "slug", help="Problem slug, hyphen-separated (e.g. trapping-rain-water)"
    )

    args = parser.parse_args()
    create_solution_folder(args.id, args.difficulty, args.slug)


if __name__ == "__main__":
    main()
