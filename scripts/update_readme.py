import os
import re

README_PATH = "README.md"
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
    if not os.path.isdir(difficulty):
        continue

    for folder in sorted(os.listdir(difficulty)):
        folder_path = os.path.join(difficulty, folder)
        if not os.path.isdir(folder_path):
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

with open(README_PATH, "r", encoding="utf-8") as f:
    content = f.read()

pattern = re.compile(
    r"\| # \| Problem \| Difficulty \| Solution \|[\s\S]*?\n\n",
    re.MULTILINE,
)

new_content, count = pattern.subn(table_md + "\n\n", content)

if count == 0:
    raise RuntimeError("Solutions table not found or malformed in README.md")

with open(README_PATH, "w", encoding="utf-8") as f:
    f.write(new_content)

print("✅ README.md updated successfully")
