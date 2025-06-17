import os
import shutil
import re
import datetime
import logging
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from tkinter import *
from tkinter import filedialog
import json
import time

class FileMovedHandler(FileSystemEventHandler):
    TEMP_EXTENSIONS = (".crdownload", ".part", ".tmp", ".download", ".opdownload", ".filepart", ".temp")
    debounce_time = 1

    def is_temp_file(self, filepath):
        _, ext = os.path.splitext(filepath)
        return ext.lower() in self.TEMP_EXTENSIONS or os.path.basename(filepath).startswith("~$")

    def on_moved(self, event):
        if event.is_directory:    
            return
        print('hotdog')
        # print(f"destination path: {event.dest_path}")
        time.sleep(self.debounce_time)
        if not self.is_temp_file(event.dest_path):
        #need to add debounce
            sort_files()
        return super().on_moved(event)
    

watch_dir = "C:\\Users\\ADMIN\\Downloads"
selected_dir = None
observer = None
file_extensions = {
    "Images": [".png", ".jpg"],
    "Videos": [".mp4", ".mov"],
    "Documents": [".docx", ".pdf", ".xslx"],
    "Fonts": [".ttf", ".otf"],
    "Others": [".zip", ".exe"],
}

def start_observer():
    global observer
    event_handler = FileMovedHandler()
    observer.schedule(event_handler=event_handler, path=watch_dir)
    observer.start() 
    print("Observer Started")
    observer.join()

def load_json():
    try:
        with open('config.json') as file:
            global file_extensions
            file_extensions = json.load(file)
            # print(f"json {file_extensions}")
    except:
        print("no json file")

def save_config():
    try:
        with open('config.json', 'x') as file:
            json.dump(file_extensions, file)
    except FileExistsError:
        with open('config.json', 'w') as file:
            json.dump(file_extensions, file)


def change_folder_name():
    pass

def select_destination():
    global watch_dir 
    watch_dir = filedialog.askdirectory()
    print('file selection')
    selected_dir.configure(text=watch_dir)
    
    

def sort_files():
    print(f"current dir {watch_dir}")
    
    for ext in file_extensions.keys():
        os.makedirs(os.path.join(watch_dir, ext), exist_ok=True)
    
    for item in os.listdir(watch_dir):
        source = os.path.join(watch_dir, item)

        if not os.path.isfile(source):
            continue

        _, ext = os.path.splitext(item)
        for directory, extension in file_extensions.items():
            
            if ext in extension:
                destination_dir = os.path.join(watch_dir, directory)
                existing_src = os.path.join(destination_dir, item)
                if os.path.exists(existing_src):
                    item_renamed = rename_file(destination_dir, item)
                    prev = source
                    source = os.path.join(watch_dir, item_renamed)
                    os.rename(prev, source)
                  
                shutil.move(src=source, dst=destination_dir)
                break
        else:
            shutil.move(src=os.path.join(watch_dir, item), dst=os.path.join(watch_dir, "Others"))

def rename_file(path:str, item:str):
    file, extension = os.path.splitext(item)
    pattern = re.fullmatch(r"(.*?)(?:\((\d+)\))?$", file)  
    n = pattern[1] 
    print(n)
    count = 0
    for num, file_name in enumerate(os.listdir(path)):
        split_name= os.path.splitext(file_name)[0]
        pat = re.fullmatch(r"(.*?)(?:\((\d+)\))?$", split_name)
        if pat[1] == n:
            count += 1
    
    file = f"{n}({count}){extension}"
    return file
def close_window():
    print("closed")
    observer.stop()
    root.destroy()


load_json()

observer = Observer()
# root = Tk()
# root.title("File Sorter")
# root.geometry("800x600")
# root.resizable(False, False)
# menu = Menu(root)
# root.config(menu=menu)
# filemenu = Menu(menu)
# menu.add_cascade(label="File", menu=filemenu)
# filemenu.add_command(label='Save', command=save_config)
# root.protocol("WM_DELETE_WINDOW", close_window)
# selector_label = Label(root, text="Select a destination")
# select_button = Button(root, text="Select", width=25, command=select_destination)
# sort_button = Button(root, text="Sort", command=sort_files)
# selected_dir = Label(root, text=watch_dir)
# selector_label.pack()
# selected_dir.pack()
# select_button.pack()
# for i in file_extensions.keys():
#     curr_label = Label(root, text=i)
#     curr_label.pack()
# sort_button.pack()


# root.mainloop()

start_observer()

