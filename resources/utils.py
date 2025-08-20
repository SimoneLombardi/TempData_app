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
    

    
def file_name_external_data(ext_dir, app_dir, filenames):
    valid = False
    while not valid:
        anno = simpledialog.askstring(
            title='Inserimento Anno',
            prompt='Inserisci l\'anno di riferimento per questi file, in cifre (es. 2023):'
        )
        if anno.isdigit() and len(anno) == 4:
            current_year = dt.now().year
            if int(anno) != current_year:
                ask_to_proceed = tk.messagebox.askyesno(
                    title='Valore Anno',
                    message=f"L'anno inserito ({anno}) non corrisponde all'anno corrente. Vuoi procedere comunque?"
                )
                if ask_to_proceed:
                    valid = True
            else:
                valid = True
        else:
            showinfo(
                title='Errore',
                message='L\'anno inserito non è valido. Riprova.'
            )
    
    valid = False
    for filename in filenames:
        while not valid:
            mese = simpledialog.askstring(
                title='Inserimento Mese',
                prompt=f'Inserisci il nome del mese relativo a questo file {os.path.basename(filename)}:'
            )
            mese = mese.lower()
            nome_mese = mese[0:3]
            if nome_mese in months_dict.keys():
                valid = True
                new_filename = f"{'0'+months_dict[nome_mese]}_{anno}_"
            else:
                showinfo(
                    title='Errore',
                    message='Il mese inserito non è valido. Riprova.'
                )
        
        os.rename(filename, (ext_dir+'/'+new_filename+'.csv'))
    
# TO DO inserire nome file completo e fare controllo su nome file
def file_name_sensor_data(sens_dir, app_dir, filenames):
    valid = False
    for filename in filenames:
        while not valid:
            sensor_name = simpledialog.askstring(
                title='Inserimento nome sensore',
                prompt=f'Inserisci il nome del sensore relativo a questo file {os.path.basename(filename)}:'
            )
            
        
        os.rename(filename, (sens_dir+'/'+new_filename+'.csv'))