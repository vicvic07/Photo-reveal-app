import os
import random
import tkinter as tk
from tkinter import messagebox
import sys
files=[]
def init (folder):
    global files
    files=[f for f in os.listdir (folder) if f.lower().endswith(('.png', '.jpeg', '.jpg'))]
    if not files:
        messagebox.showerror ("Error", "Folderul nu contine poze sarmaluitoare! :(")
        sys.exit()
def getPhoto (folder):
    global files
    if not len (files):
        return -1
    else:
        new_path=random.choice (files)
        files.remove (new_path)
        return folder+r'\\'+new_path