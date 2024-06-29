import os
import sys
import shutil
import logging
import datetime
#import zipfile

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='backup.log')

def backup():
    setup_logging()

    try:
        print("File Backup has started")
        src = input("Please enter the source path(Absolute path):").strip()
        if not os.path.isdir(src):
            logging.error(f"Source file not found at {src}.")
            print(f"Please enter a valid Absolute path. As {src} is not a valid directory with absolute path.")
            return

        dest = input("Please enter the Destination path(Absolute path):").strip()
        if not os.path.isdir(dest):
            ans = input("Will you like to create this destination directory as it is not avaliable(Y/N):").strip()
            if ans.lower() == 'y':
                os.makedirs(dest)
                logging.info(f"Destination folder created successfully at {dest}.")
            else:
                logging.error(f"Please enter a valid Absolute path. As {dest} is not a valid directory with absolute path.")
                return
            
        print("Files and folders in source file are:")
        for file in os.listdir(src):
            print(f"- {file}")
        print(f"Total number of files in source: {len(os.listdir(src))} files")
        print("Enter the type of backup:","1. Making an archive","2. Copying all files into destination.")

        choice = input("Enter your choice(1-2):").strip()

        if choice not in ['1','2']:
            logging.error("Please enter a valid number.")
            return
        
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S_%f')
        backup_name = os.path.join(dest,f'backup_{timestamp}')
            
        if choice == '1':
            #with zipfile.ZipFile(backup_name, 'a', zipfile.ZIP_DEFLATED) as zipf:
            #    for root, dirs, files in os.walk(src):
            #        for file in files:
            #            file_path = os.path.join(root, file)
            #            arcname = os.path.relpath(file_path, src)
            #            print(f"Adding {arcname} to archive...")
            #            zipf.write(file_path, arcname)

            shutil.make_archive(base_name=backup_name, format='zip', root_dir=src)
            logging.info(f"Backup created successfully: {backup_name}.zip")
            print(f"Backup created successfully at {backup_name}.zip")
        else:
            print("Starting backup")
            shutil.copytree(src,backup_name)
            logging.info(f"Backup created successfully: {backup_name}")
            print(f"Backup created successfully at {backup_name}")

    except Exception as e:
        logging.error(f"Error during backup: {e}")
        print(f"Error during backup: {e}")
if __name__ == "__main__":
    backup()
