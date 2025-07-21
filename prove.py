import csv
import datetime as dt
import time as tm 
import pytz
import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

import tkinter as tk
from tkinter import ttk

months = [('gen', '1'), ('feb', '2'), ('mar', '3'), ('apr', '4'), ('mag', '5'), ('giu', '6'), ('lug', '7'), ('ago', '8'), ('set', '9'), ('ott', '10'), ('nov', '11'), ('dic', '12')]
day_ita = [('Monday', 'Lunedì'), ('Tuesday', 'Martedì'), ('Wednesday', 'Mercoledì'), ('Thursday', 'Giovedì'), ('Friday', 'Venerdì'), ('Saturday', 'Sabato'), ('Sunday', 'Domenica')]
sensors = ['TH_4_09', 'TH_4_13', 'TH_4_06', 'TH_4_01', 'TH_4_02', 'TH_3_25', 'TH_3_28', 'TH_3_27', 'TH_3_03', 'TH_3_02', 'TH_3_01', 'TH_3_12', 'TH_3_16', 'TH_1_10', 'TH_1_12', 'TH_1_43', 'TH_T_10', 'TH_1_96','TH_1_106','TH_1_89','TH_2_42','TH_2_89', 'TH_2_105']
monts_dict = dict(months)
day_ita_dict = dict(day_ita)

filename = '07_2025_.csv'  # Example file name
with open('07_2025_.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    raw_data_set = list(reader)
    
    print("\n\n\n")
    data_parts = list()
    data_string_split = filename.split('_')
    data_parts = ['-1', data_string_split[0], data_string_split[1]]
    
    
    timestamp_day = list()
    tmin = list()
    tmax = list()
    
    for row in raw_data_set[1:]:
        day = row[0].split()[1]
        data_parts[0] = day
        data_string = ' '.join(data_parts)
        
        print(f"after join {data_string}")
        
        timestamp_day.append(dt.datetime.strptime(data_string, '%d %m %Y'))
        tmin.append(float(row[2]))
        tmax.append(float(row[3]))
    
    
    print(timestamp_day[3], tmin[3], tmax[3])
    