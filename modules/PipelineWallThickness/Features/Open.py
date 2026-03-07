import pandas as pd
from tkinter import filedialog
import random

from PyQt5.QtWidgets import QMessageBox

def fileread(open_List):
    print(f"\n\t Opening your file please wait..!!")
    try:
        
        filepath = filedialog.askopenfilename(
                initialdir="C:/Users/DELL/Desktop",
                title= "Open csv file...!!",
                defaultextension= "*.csv",
                filetypes=(
                    ("csv file","*.csv"),
                    ("HTML file","*.html"),
                    ("text file","*.txt"),
                    ("All file","*.*")
                )
            )
    except:
        print(f"error code:{random.random()}>>>>>>>Error in opening the file...@@@$$%%%")
    try:
            if filepath is None:
                return
            else:
                with open(filepath,'r'):
                    df = pd.read_csv(filepath)
                    column_To_Read = df["Values"].tolist()
                    open_List.clear()
                    open_List.extend(column_To_Read)
    except:
            print(f"error code:{random.random()}>>>>>>ERROR in opening your file...!!")