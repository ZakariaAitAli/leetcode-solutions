import os
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
README_PATH = REPO_ROOT / "README.md"
DIFFICULTIES = ["easy", "medium", "hard"]

solutions = []


def format_title(slug: str) -> str:
    words = slug.split("-")
    lowercase_words = {"of", "with", "and", "to", "in", "for", "at", "by"}
    title = []
    for i, w in enumerate(words):
        if i != 0 and w in lowercase_words:
            title.append(w)
        else:
            title.append(w.capitalize())
    return " ".join(title)


for difficulty in DIFFICULTIES:
    difficulty_path = REPO_ROOT / difficulty
    if not difficulty_path.is_dir():
        continue

    for folder in sorted(os.listdir(difficulty_path)):
        folder_path = difficulty_path / folder
        if not folder_path.is_dir():
            continue

        match = re.match(r"^(\d+)-(.+)$", folder)
        if not match:
            continue

        problem_number = int(match.group(1))
        slug = match.group(2)

        title = format_title(slug)
        solution_link = f"{difficulty}/{folder}/solution.py"

        solutions.append(
            (problem_number, title, difficulty.capitalize(), solution_link)
        )

solutions.sort(key=lambda x: x[0])

table = [
    "| # | Problem | Difficulty | Solution |",
    "|:-:|--------|:----------:|:--------:|",
]

for num, title, diff, link in solutions:
    table.append(f"| {num} | {title} | {diff} | [Python]({link}) |")

table_md = "\n".join(table)

content = README_PATH.read_text(encoding="utf-8")

pattern = re.compile(
    r"(\|[^\n]*#[^\n]*\|[^\n]*\n(?:\|[^\n]*\n)+)\n",
    re.MULTILINE,
)

new_content, count = pattern.subn(table_md + "\n\n", content)

if count == 0:
    raise RuntimeError("Solutions table not found or malformed in README.md")

README_PATH.write_text(new_content, encoding="utf-8")

print("README.md updated successfully")
