import os
import shutil
import datetime
import logging

from tkinter import *
from tkinter import filedialog

dir = "/"
items = list()
file_extensions = {
    "Images": [".png", ".jpg"],
    "Videos": [".mp4", ".mov"],
    "Documents": [".docx", ".pdf", ".xslx"],
    "Others": [".zip", ".exe"]
}

def change_folder_name():
    pass

def select_destination():
    global dir 
    global items
    dir = filedialog.askdirectory()
    print('file selection')
    selected_dir.configure(text=dir)
    items= os.listdir(dir)

def sort_files():
    for ext in file_extensions.keys():
        os.makedirs(os.path.join(dir, ext), exist_ok=True)
    
    for item in items:
        if os.path.isfile(os.path.join(dir, item)):
            name, ext = os.path.splitext(item)
            for directory, extension in file_extensions.items():
                if ext in extension:
                    shutil.move(src=os.path.join(dir, item), dst=os.path.join(dir, directory))
                    break
            else:
                shutil.move(src=os.path.join(dir, item), dst=os.path.join(dir, "Others"))
    
root = Tk()
root.title("File Sorter")
root.geometry("800x600")
root.resizable(False, False)
selector_label = Label(root, text="Select a destination")

select_button = Button(root, text="Select", width=25, command=select_destination)
sort_button = Button(root, text="Sort", command=sort_files)
selected_dir = Label(root, text=dir)
selector_label.pack()
sort_button.pack()
selected_dir.pack()
select_button.pack()
for i in file_extensions.keys():
    curr_label = Label(root, text=i)
    curr_label.pack()
root.mainloop()

