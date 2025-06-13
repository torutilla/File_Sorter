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
}
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
        print("sorted")
    # for item in items:
    #     name, ext = os.path.splitext(item)
        

        

root = Tk()
root.title("File Sorter")
root.geometry("800x600")
root.resizable(False, False)
selector_label = Label(root, text="Select a destination")

select_button = Button(root, text="Select", width=25, command=select_destination)
sort_button = Button(root, text="Sort", command=sort_files)
sort_button.grid(row=1, column=1)
selected_dir = Label(root, text=dir)
selector_label.grid(row=0, column=0)
select_button.grid(row=0, column=1)
selected_dir.grid(row=1, column=0)
root.mainloop()

