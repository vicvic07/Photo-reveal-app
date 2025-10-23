import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import sys
def path ():
    root=tk.Tk()
    root.withdraw ()
    folder=filedialog.askdirectory (title="Director folder poze sarmaluitoare")
    if not folder:
        messagebox.showerror ("Error", "Nu a fost selectat un folder sarmaluitor! :(")
        sys.exit ()
    return folder