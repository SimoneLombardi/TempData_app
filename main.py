import csv
import datetime as dt
import time as tm 
import pytz
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import os
import numpy as np

import tkinter as tk
from tkinter import ttk

import resources.utils as utils

sensor_data_delimiter = ';'
exeternal_data_delimiter = ','
space_delimiter = ' '
hour_delimiter = ':'

months = [('gen', '1'), ('feb', '2'), ('mar', '3'), ('apr', '4'), ('mag', '5'), ('giu', '6'), ('lug', '7'), ('ago', '8'), ('set', '9'), ('ott', '10'), ('nov', '11'), ('dic', '12')]
day_ita = [('Monday', 'Lunedì'), ('Tuesday', 'Martedì'), ('Wednesday', 'Mercoledì'), ('Thursday', 'Giovedì'), ('Friday', 'Venerdì'), ('Saturday', 'Sabato'), ('Sunday', 'Domenica')]
monts_dict = dict(months)
day_ita_dict = dict(day_ita)

def main():
    print("\n\n\n Starting the temperature data plotting script.")
    # step 1: load data from cvs files folder
    dati_dir = 'dati/'
    dati_sensori_dir = 'dati_sensori/'
    dati_esterni_dir = 'dati_esterni/'
    
    current_file_dataframe = pd.DataFrame()
    current_file_dataframe_ext = pd.DataFrame()
    data_frame_ext = pd.DataFrame({
        'timestamp_day': [],
        'Temp min': [],
        'Temp max': []
    })
    
    try:
        data_frame_ext = pd.read_pickle('resources/saved_data/dati_esterni.pkl')
    except FileNotFoundError:
        pass
        
    
    for filename in os.listdir(dati_dir + dati_esterni_dir):
        #print(filename)
        if utils.check_file_name(filename):                                           
            filepath = os.path.join(dati_dir + dati_esterni_dir, filename)
            #print(filepath)
            # save here the data, check for correct temperature colum
            timestamp_day = list()
            col_1_lst = list()
            col_2_lst = list()
            
            with open(filepath, 'r') as csvfile:
                reader = csv.reader(csvfile, delimiter=exeternal_data_delimiter)
                raw_data_set = list(reader)
                
                data_string_split = filename.split('_')
                data_parts = ['-1', data_string_split[0], data_string_split[1]]
                
                for row in raw_data_set[1:]:
                    
                    day = row[0].split()[1]
                    data_parts[0] = day
                    data_string = ' '.join(data_parts)          
                    
                    timestamp_day.append(dt.datetime.strptime(data_string, '%d %m %Y'))
                    try:
                        temp1 = float(row[2])
                        temp2 = float(row[3])
                    except ValueError:
                        temp1 = np.nan
                        temp2 = np.nan
                        
                    col_1_lst.append(temp1)
                    col_2_lst.append(temp2)
                    
            current_file_dataframe_ext = pd.DataFrame({
                'timestamp_day': timestamp_day,
                'Temp min': col_1_lst,
                'Temp max': col_2_lst
            })
                
            data_frame_ext = pd.concat([data_frame_ext, current_file_dataframe_ext], ignore_index=True)
            
            print(f"Data from {filename} processed. Total records: {current_file_dataframe_ext.shape}")
            print(f"complete ext data frame shape: {data_frame_ext.shape}")
            
    # save the dataFrame to a csv file
    data_frame_ext.sort_values(by='timestamp_day', inplace=True, kind='stable')
    data_frame_ext.drop_duplicates(subset=['timestamp_day'], inplace=True, keep='first')
    data_frame_ext.dropna(subset=['Temp min', 'Temp max'], inplace=True, axis=0)
    data_frame_ext.reset_index(drop=True, inplace=True)
    
    print(f"complete ext data frame shape BEFORE SAVE: {data_frame_ext.shape}")
    data_frame_ext.to_pickle('resources/saved_data/dati_esterni.pkl')
    
    for filename in os.listdir(dati_dir + dati_sensori_dir):
        #print(filename)
        if utils.check_file_name(filename):                                           # da modificare con funzione per vedere se nome corretto
            filepath = os.path.join(dati_dir + dati_sensori_dir, filename)
            #print(filepath)
            # save here the data, check for correct temperature colum
            timestamp_day = list()
            timestamp_hour = list()
            col_1_lst = list()
            col_2_lst = list()
            
            with open(filepath, 'r') as csvfile:
                reader = csv.reader(csvfile, delimiter=sensor_data_delimiter)
                raw_data_set = list(reader)
                
                for row in raw_data_set[1:]:  # start from 1 to skip the header
                    data_string_split = row[0].replace(',', '').replace(':', ' ').split()
                    
                    day = [data_string_split[0], monts_dict[data_string_split[1]], data_string_split[2]]
                    hour = [data_string_split[3], data_string_split[4]]
                    
                    day = space_delimiter.join(day)
                    hour = hour_delimiter.join(hour)
                    
                    timestamp_day.append(dt.datetime.strptime(day, '%d %m %Y'))
                    timestamp_hour.append(hour)
                    col_1_lst.append(float(row[1].replace(',', '.')))
                    col_2_lst.append(float(row[2].replace(',', '.')))
                    
                #print(len(timestamp_day), sum(col_1_lst)/len(col_1_lst), sum(col_2_lst)/len(col_2_lst))
                col_1_avg = sum(col_1_lst) / len(col_1_lst)
                col_2_avg = sum(col_2_lst) / len(col_2_lst)
                
                if col_1_avg < col_2_avg:                   # temperature is in column 1
                    current_file_dataframe = pd.DataFrame({
                        'timestamp_day': timestamp_day,
                        'timestamp_hour': timestamp_hour,
                        'Temperature': col_1_lst,
                        'Humidity': col_2_lst
                    })
                else:                                       # temperature is in column 2
                    current_file_dataframe = pd.DataFrame({
                        'timestamp_day': timestamp_day,
                        'timestamp_hour': timestamp_hour,
                        'Temperature': col_2_lst,
                        'Humidity': col_1_lst
                    })

            unique_dates = current_file_dataframe['timestamp_day'].unique()
            print(f"Unique dates: {len(unique_dates)}")
            
            for date in unique_dates:
                maxmin_temp = 1
                plot_data_frame = current_file_dataframe[current_file_dataframe['timestamp_day'] == date]
                ext_temp_data = data_frame_ext[data_frame_ext['timestamp_day'] == date]
                if ext_temp_data.empty:
                    #print(f"No external data for date: {date.strftime('%Y-%m-%d')}")
                    maxmin_temp = 0
                
                #print(f"plot dataframe:\n {plot_data_frame.head()}")
                #print(f"ext temp data:\n {ext_temp_data.head()}")
                
                fig, ax = plt.subplots(figsize=(10, 5))
                ax.plot(plot_data_frame['timestamp_hour'], plot_data_frame['Temperature'], marker='o', linestyle='dashed', color='k')
                ax.grid(True, linestyle='solid', alpha=0.3)
                
                x_start, x_end = ax.get_xlim()
                    
                if maxmin_temp != 0:
                    mintemp = ax.hlines(ext_temp_data['Temp min'],xmin=x_start,xmax=x_end, color='b', linestyle='dashdot', linewidth=0.5)
                    maxtemp = ax.hlines(ext_temp_data['Temp max'],xmin=x_start,xmax=x_end, color='r', linestyle='dashdot', linewidth=0.5)
                    ax.legend([mintemp, maxtemp],[f"Temp min: {ext_temp_data['Temp min'].item()}", f"Temp max: {ext_temp_data['Temp max'].item()}"],loc='best', fontsize=7)
                
                y_start, y_end = ax.get_ylim()
                
                for x, y in zip(plot_data_frame['timestamp_hour'], plot_data_frame['Temperature']):
                    yinter = y_end-y_start
                    #print(y_start, y_end, yinter)
                    ypos = y + (yinter*0.02) if y + (yinter*0.02) < y_end else y - (yinter*0.035)
                    ax.text(x, ypos, f'{y:.1f}', fontsize=7, ha='center', color='black')
                
                ax.set_xticks(plot_data_frame['timestamp_hour'])
                ax.set_xticklabels(plot_data_frame['timestamp_hour'], rotation=45)
                
                day_name = date.day_name()
                sensor_name = filename.split('.')[0]
                day_name_ita = day_ita_dict.get(day_name)
                file_name = f"{date.strftime('%d-%m-%Y')}"+ f" {day_name_ita}"
                ttlString = f"{date.strftime('%d-%m-%Y')}"+ f" {day_name_ita}" + f", sensore:{sensor_name}"
                ax.set_title(ttlString)
                ax.set_xlabel('Time of Day')
                ax.set_ylabel('Temperature (°C)')
                
                if not os.path.exists("output/plots/" + sensor_name):
                    os.makedirs("output/plots/" + sensor_name)
                
                path = "output/plots/" + sensor_name + "/" + file_name + ".png"
                fig.savefig(path, dpi=300, bbox_inches='tight')
                plt.close(fig)  # Close the figure to free memory      
                
            ##print(current_file_dataframe['timestamp_hour'].head())
            ##print(current_file_dataframe.shape)
            
                    

                
                    
            
            
    
if __name__ == "__main__":
    main()