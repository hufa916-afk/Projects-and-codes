import os

FOLDER_PATH = "/path/to/folder"

for root, dirs, files in os.walk(FOLDER_PATH, topdown=False):
    for d in dirs:
        dir_path = os.path.join(root, d)
        if not os.listdir(dir_path):  # Check if folder empty
            os.rmdir(dir_path)
            print(f"Deleted empty folder: {dir_path}")
