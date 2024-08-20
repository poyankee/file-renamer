# File Renamer

This Python script allows you to rename all files in a selected directory by numbering them sequentially. It uses the `os` module to handle file renaming and `tkinter` for directory selection.

## Features

- Renames all files in a selected directory with sequential numbers.
- Supports various file types by preserving their extensions.
- Easy-to-use graphical interface for selecting the directory.

## Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/file-renamer.git
2. **Navigate to the repository directory:**
   ```bash
    cd file-renamer
3. **Run the script:**
   ```bash
    python file_renamer.py

## Requirements
- Python 3.x
- tkinter (usually comes pre-installed with Python)

## How It Works
- The script first prompts the user to select a directory using a graphical file dialog.
- It then walks through all the files in the directory, renaming them with sequential numbers while preserving the file extensions.
- The process is logged in the console, and a "Completed" message is displayed once all files are renamed.

## Contributing
Feel free to fork this repository, create a branch, and submit a pull request if you would like to contribute!
