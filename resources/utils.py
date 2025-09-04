import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter import simpledialog
from datetime import datetime as dt

import os

months = [('gen', '1'), ('feb', '2'), ('mar', '3'), ('apr', '4'), ('mag', '5'), ('giu', '6'), ('lug', '7'), ('ago', '8'), ('set', '9'), ('ott', '10'), ('nov', '11'), ('dic', '12')]
months_dict = dict(months)


def check_file_name(filename):
    print(f"Checking file name: {filename}")
    
    if filename.endswith('.csv'):
        #print("File name is valid.")
        return True
    else:
        #print("File name is invalid. It should end with '.csv'.")
        return False
    

    

        
       