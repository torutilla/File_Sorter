import os
import shutil
import datetime
import logging
from tkinter import *


def main():
    root = Tk()
    root.title("File Selector")
    
    selector_label = Label(root, text="Select a destination")
    selector_label.pack()

    select_button = Button(root, text="Select", width=25, command=select_destination)
    select_button.pack()
    root.mainloop()


def select_destination():
    print('file selection')
    pass

main()