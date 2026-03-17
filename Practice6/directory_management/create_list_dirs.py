import os

# Create nested directories
os.makedirs('parent_dir/sub_dir/child_dir', exist_ok=True)
print("Nested directories created.")


import os

# List all files and folders in the current directory
files_and_folders = os.listdir('.')
print(files_and_folders)


import os

# Find all files with .txt extension in the current directory
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print("Text files:", txt_files)