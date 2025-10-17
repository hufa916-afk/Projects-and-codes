import os
import shutil

FOLDER = "/user/arundhati.jalaj/Downloads"

file_types = {
    "Images": [".png", ".jpg", ".jpeg"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Compressed": [".zip", ".tar", ".gz"],
    "Videos": [".mp4", ".mkv"],
}

for filename in os.listdir(FOLDER):
    file_path = os.path.join(FOLDER, filename)

    if os.path.isfile(file_path):
        for folder, extensions in file_types.items():
            if filename.lower().endswith(tuple(extensions)):
                target_folder = os.path.join(FOLDER, folder)
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, target_folder)
                print(f"Moved {filename} to {folder}")
