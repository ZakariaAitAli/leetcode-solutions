import os

# Path to the main README.md
README_PATH = "README.md"

# Folders to scan
difficulty_levels = ["easy", "medium", "hard"]

# Collect solutions
solutions = []

for difficulty in difficulty_levels:
    path = os.path.join(difficulty)
    if os.path.exists(path):
        for folder in sorted(os.listdir(path)):
            folder_path = os.path.join(path, folder)
            if os.path.isdir(folder_path):
                # Extract problem number and title
                parts = folder.split('-')
                problem_number = parts[0]
                title = ' '.join(parts[1:]).title()
                solution_link = f"{difficulty}/{folder}/solution.py"
                solutions.append((problem_number, title, difficulty.capitalize(), solution_link))

# Sort solutions by problem number
solutions.sort(key=lambda x: int(x[0]))

# Build the Solutions Table Markdown
table_header = "| # | Problem | Difficulty | Solution |\n|:-:|:--------|:----------:|:--------:|\n"
table_rows = ""
for problem_number, title, difficulty, link in solutions:
    table_rows += f"| {problem_number} | {title} | {difficulty} | [Python]({link}) |\n"

# Read the current README
with open(README_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the old Solutions Table
start_marker = "| # | Problem | Difficulty | Solution |"
end_marker = "*(I will keep updating this table as I solve more problems.)*"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + table_header + table_rows + "\n\n" + content[end_idx:]
else:
    print("Couldn't find the Solutions Table in README.md. Please check the format.")
    exit()

# Write back the updated README
with open(README_PATH, "w", encoding="utf-8") as f:
    f.write(new_content)

print("✅ README.md updated successfully!")
