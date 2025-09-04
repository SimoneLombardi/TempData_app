import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter import simpledialog

import resources.utils as utils

import re
import os

dati_esterni_dir = os.getcwd() + '/dati/dati_esterni/'
dati_sensori_dir = os.getcwd() + '/dati/dati_sensori/'
app_dir = os.getcwd() 


def load_file_ext():
    filetypes = (
        ('text files', '*.csv'),
        ('All files', '*.*')
    )

    filenames = fd.askopenfilenames(
        title='Open files',
        initialdir='/home/simone/Desktop/prova 150h/TempData_app',
        filetypes=filetypes)
    
    utils.file_name_external_data(dati_esterni_dir, app_dir, filenames)
    
    msg = "EXTERNAL DATA FILES LOADED"
    showinfo(
        title='Selected Files '+ msg,
        message=filenames
    )
    
def load_file_sens():
    filetypes = (
        ('text files', '*.csv'),
        ('All files', '*.*')
    )

    filenames = fd.askopenfilenames(
        title='Open files',
        initialdir='/home/simone',
        filetypes=filetypes)

    msg = "SENSOR DATA FILES LOADED"
    showinfo(
        title='Selected Files '+ msg,
        message=filenames
    )

def main():
    #print("hello")
    print(dati_esterni_dir)
    
    # bottni 1(carica file dati esterni), 2(carica file dati sensori), seleziona nuove impostazioni
    # lista impostazioni: intervallo orario, dati temp esterna
    #                     seleziona quali sensori fare il plot
    
    root = tk.Tk() 
    
    external_data_btt = tk.Button(root, text="Carica file dati esterni", command=load_file_ext)
    sensor_data_btt = tk.Button(root, text="Carica file dati sensori", command=load_file_sens)
    launch_program_btt = tk.Button(root, text="Lancia programma", command=lambda: showinfo("Launch", "Program launch not implemented yet."))
    settings_btt = tk.Button(root, text="Impostazioni", command=lambda: showinfo("Settings", "Settings dialog not implemented yet."))
    
    external_data_btt.pack(padx=5, pady=5, expand=True, fill=tk.BOTH)
    sensor_data_btt.pack(padx=5, pady=5, expand=True, fill=tk.BOTH)
    launch_program_btt.pack(padx=5, pady=5, expand=True, fill=tk.BOTH)
    settings_btt.pack(padx=5, pady=5, expand=True, fill=tk.BOTH)
        
    root.mainloop()
    
if __name__ == "__main__":
    main()