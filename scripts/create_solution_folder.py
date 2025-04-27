import os

# Function to create the folder and files inside the appropriate category
def create_solution_folder(problem_name, difficulty):
    # Ensure valid difficulty input
    if difficulty not in ['easy', 'medium', 'hard']:
        print("Error: Please specify a valid difficulty ('easy', 'medium', 'hard').")
        return

    # Convert the problem name into a folder-friendly format (lowercase, hyphen-separated)
    folder_name = problem_name.lower().replace(' ', '-').replace('.', '')

    # Define the base path (path to the 'leetcode-solutions' folder)
    base_path = os.path.abspath(os.path.join(os.getcwd(), '..'))  # Goes one directory up from 'scripts/'

    # Create the full path for the new folder inside the chosen difficulty
    difficulty_folder_path = os.path.join(base_path, difficulty)
    os.makedirs(difficulty_folder_path, exist_ok=True)
    
    # Full path for the solution folder
    solution_folder_path = os.path.join(difficulty_folder_path, folder_name)
    
    # Create the folder
    os.makedirs(solution_folder_path, exist_ok=True)

    # Define paths for the solution and README files
    solution_file_path = os.path.join(solution_folder_path, 'solution.py')
    readme_file_path = os.path.join(solution_folder_path, 'README.md')

    # Create the solution.py file with a basic template
    with open(solution_file_path, 'w', encoding='utf-8') as solution_file:
        solution_file.write(f"""
# {problem_name}
Difficulty: {difficulty.capitalize()}

class Solution:
    def solve(self):
        pass  # Your solution here
""")

    # Create the README.md file with a basic template
    with open(readme_file_path, 'w', encoding='utf-8') as readme_file:
        readme_file.write(f"""
# {problem_name}

## Problem

**Problem description goes here.**

---

## Example

**Input:**  
Example input here.

**Output:**  
Example output here.

---

## Approach

- Step 1: Describe your approach.
- Step 2: Elaborate on your solution steps.
- Step 3: Mention time and space complexity.

---

## Solution

[solution.py](./solution.py)
""")

    print(f"✅ Folder created: {solution_folder_path}/")
    print(f"✅ Files created: {solution_file_path} and {readme_file_path}")

# Input: Problem name and difficulty
problem_name = input("Enter the problem name: ")
difficulty = input("Enter the difficulty ('easy', 'medium', 'hard'): ").lower()

create_solution_folder(problem_name, difficulty)
