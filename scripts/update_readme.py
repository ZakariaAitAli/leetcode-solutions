import os

# Define the root directory for the LeetCode solutions
root_dir = os.getcwd()

# Function to update README.md files
def update_readme():
    # Loop through all difficulty folders (easy, medium, hard)
    for difficulty in ['easy', 'medium', 'hard']:
        difficulty_folder = os.path.join(root_dir, difficulty)

        # Check if the folder exists
        if os.path.exists(difficulty_folder):
            # Loop through each folder (problem solution) inside the difficulty folder
            for folder_name in os.listdir(difficulty_folder):
                problem_folder_path = os.path.join(difficulty_folder, folder_name)
                readme_path = os.path.join(problem_folder_path, 'README.md')

                # If the README.md file exists, update it
                if os.path.exists(readme_path):
                    with open(readme_path, 'a', encoding='utf-8') as readme_file:
                        readme_file.write("\n\n# Updated at commit time\n")
                        readme_file.write("Automated update: Added more description or instructions.\n")
                    print(f"✅ Updated README.md for {folder_name}")
                else:
                    print(f"⚠️ README.md not found for {folder_name}")
        else:
            print(f"⚠️ Difficulty folder {difficulty} not found")

# Call the function to update the README
update_readme()
