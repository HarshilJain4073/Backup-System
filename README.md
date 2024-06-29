# File Backup System

This Python script allows you to back up files from a source directory to a destination directory. It provides options to either create a zip archive of the source files or copy them directly to the destination.

## Requirements
- Python 3.x
- `os`, `sys`, `shutil`, `logging`, `datetime` modules

## Setup
1. **Clone Repository**: Clone this repository to your local machine.
   
2. **Install Python**: Make sure Python 3.x is installed on your system.

3. **Dependencies**: Install required Python modules using pip:
   ```bash
   pip install -r requirements.txt
   
## Usage

### Run the Script
Execute the script in your terminal or command prompt:

    ```bash
    python backup_script.py

## Follow the Prompts

1. **Enter the absolute path of the source directory.**
   
2. **Specify the destination directory or create one if it doesn't exist.**
   
3. **Choose between creating a zip archive (1) or copying files directly (2).**

## Backup Operation

- The script will perform the selected backup operation.
- Logs are stored in `backup.log` detailing backup success or errors.

## Features
- **Automated Timestamps:** Each backup operation is timestamped for the organization.
- **Error Handling:** Logs errors encountered during the backup process.
- **Interactive Interface:** Guides users through directory selection and backup type.

## Example

    $ python backup_script.py
    File Backup has started
    Please enter the source path(Absolute path): /path/to/source
    Please enter the Destination path(Absolute path): /path/to/destination
    Files and folders in source file are:
    - file1.txt
    - file2.jpg
    Total number of files in source: 2 files
    Enter the type of backup:
    1. Making an archive
    2. Copying all files into destination.
    Enter your choice(1-2): 1
    Backup created successfully at /path/to/destination/backup_20240629_164530_123456.zip
