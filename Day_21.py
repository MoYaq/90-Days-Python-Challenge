#Day 21: Automating Tasks with Python
#Project: Automatically Organizing Files in a Folder
#A program to demonstrate file automation using Python’s os and shutil libraries.

#Step 1: Import the necessary libraries
import os
import shutil

#Step 2: Get the folder path in Replit (if you are using your phone, if not skip this step)
def get_folder_path():
    folder_path = os.getcwd()#Gets the current working directory
    print(f"Current Folder Path: {folder_path}")
    return folder_path

#Step 3: Organize files by extension
def organize_files(folder_path):
    # List all files in the directory
    files = os.listdir(folder_path)

#Step 4: Define categories based on file extensions
    categories = {
        "TextFiles": [".txt", ".md"],
        "Images": [".jpg", ".jpeg", ".png"],
        "PDFs": [".pdf"],
        "PythonScripts": [".py"]
    }

#Step 5: Create folders if they don’t exist
    for category in categories.keys():
        category_path = os.path.join(folder_path, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

#Step 6: Move files to the correct folders
    for file in files:
        file_path = os.path.join(folder_path, file)

#Ensure it's a file and not a directory
        if os.path.isfile(file_path):
            for category, extensions in categories.items():
                if any(file.lower().endswith(ext) for ext in extensions):
                    shutil.move(file_path, os.path.join(folder_path, category, file))
                    print(f"Moved: {file} → {category}/")

#Step 7: Main program execution
if __name__ == "__main__":
    print("📂 File Organizer Program")
    
#Get the folder path inside Replit
    folder_path = get_folder_path()

#Organize the files
    organize_files(folder_path)

    print("\nFile organization complete!")