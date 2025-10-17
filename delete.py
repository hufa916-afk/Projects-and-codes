import os
import time

FOLDER_PATH = "/path/to/folder"

# 🔹 Time threshold: 1 year (in seconds)
ONE_YEAR = 365 * 24 * 60 * 60
current_time = time.time()

for filename in os.listdir(FOLDER_PATH):
    file_path = os.path.join(FOLDER_PATH, filename)

    # Skip if not a file
    if not os.path.isfile(file_path):
        continue

    # Get file's last modified time
    file_age = current_time - os.path.getmtime(file_path)

    if file_age > ONE_YEAR:
        print(f"Deleting: {file_path}")
        os.remove(file_path)  # 🚨 Comment this line if you only want to test
