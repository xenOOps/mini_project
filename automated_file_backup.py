import os
import shutil
import datetime
import schedule
import time

source=input("Enter the source path: ")
destination=input("Enter the destination path: ")

def copy_folderto_directory(source,dest):
    today=datetime.date.today()
    dest_dir=os.path.join(dest,str(today))
    try:
        shutil.copytree(source,dest_dir)
        print(f"Folder copied to {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in {dest}")

schedule.every().day.at("13:03").do(lambda: copy_folderto_directory(source,destination))
while True:
    schedule.run_pending()
    time.sleep(60)        
