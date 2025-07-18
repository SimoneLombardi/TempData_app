import lib.utils
import lib.load_data
import lib.plotter

from tkinter import *
from tkinter import ttk

class MenuFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        
        #self.configure(borderwidth=2, relief="groove")
        
        self.bttn_style = ttk.Style()
        self.bttn_style.configure("big.TButton", font=("Helvetica", 16), padding=30, width=20)
        self.bttn_padding = (10, 5)
        
        self.loadDataButton = ttk.Button(self, text="Carica nuovi dati", command=lambda: print("Load Data Clicked"), style="big.TButton")
        self.loadDataButton.grid(row=1, column=0, padx=self.bttn_padding[0], pady=self.bttn_padding[1]) 
        
        self.plotDataButton = ttk.Button(self, text="Grafica dati", command=lambda: print("Plot Data Clicked"), style="big.TButton")
        self.plotDataButton.grid(row=2, column=0, padx=self.bttn_padding[0], pady=self.bttn_padding[1])
        
        self.showRulesButton = ttk.Button(self, text="Mostra regole", command=lambda: print("Show Rules Clicked"), style="big.TButton")
        self.showRulesButton.grid(row=3, column=0, padx=self.bttn_padding[0], pady=self.bttn_padding[1])
        

class App(Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Grafici dati Temperatura")
        #self.geometry("1000x1000") 
        self.resizable(False, False) 
        
        self.menu_frame = MenuFrame(self)
        self.menu_frame.grid(row=0, column=0)