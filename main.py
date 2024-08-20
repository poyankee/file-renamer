import os
import tkinter as tk
from tkinter import filedialog

def select_directory():
    root = tk.Tk()
    root.withdraw()  
    directory_path = filedialog.askdirectory()  
    return directory_path

def rename_files_with_numbers(directory_path):
    counter = 1  

    for root, _, files in os.walk(directory_path):
        for file_name in files:
            old_file_path = os.path.join(root, file_name)
            file_extension = os.path.splitext(file_name)[1]
            new_file_name = f"{counter}{file_extension}"
            new_file_path = os.path.join(root, new_file_name)
            os.rename(old_file_path, new_file_path)
            counter += 1

    print("Completed")

if __name__ == "__main__":
    directory_path = select_directory()  
    if directory_path:  
        rename_files_with_numbers(directory_path)
    else:
        print("File path not selected.")
