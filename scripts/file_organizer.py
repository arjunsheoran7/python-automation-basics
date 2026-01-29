import os
import shutil

# Path of the folder to organize
TARGET_FOLDER = "sample_folder"

# File type categories
FILE_TYPES = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Documents": [".pdf", ".txt", ".docx"],
    "Audio": [".mp3", ".wav"],
    "Videos": [".mp4", ".mov"]
}

# Create category folders if they don't exist
for folder in FILE_TYPES:
    folder_path = os.path.join(TARGET_FOLDER, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Organize files
for file_name in os.listdir(TARGET_FOLDER):
    file_path = os.path.join(TARGET_FOLDER, file_name)

    if os.path.isfile(file_path):
        for folder, extensions in FILE_TYPES.items():
            if file_name.lower().endswith(tuple(extensions)):
                shutil.move(file_path, os.path.join(TARGET_FOLDER, folder, file_name))
                break
