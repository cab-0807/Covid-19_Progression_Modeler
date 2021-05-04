from tkinter import *
from tkinter import messagebox
import os



def dataAcquisition():
    os.chdir("/Users/mac/Documents/COURS/DIC2/SGBD Avancé/Projet/Covid-19_Progression_Modeler/DataAcquisition")
    os.system("python3 DataAcquisition.py")

def dataLoader():
    os.chdir("/Users/mac/Documents/COURS/DIC2/SGBD Avancé/Projet/Covid-19_Progression_Modeler/DataLoader")
    os.system("python3 DataLoader.py")

def dataExplorer():
    os.chdir("/Users/mac/Documents/COURS/DIC2/SGBD Avancé/Projet/Covid-19_Progression_Modeler/DataExplorer")
    os.system("python3 DataExplorer.py")

my_w=Tk()
my_w.title("COVID-19 PROGRESSION MODELER")
my_w.geometry("307x130")
var = StringVar()
lbl = Label(my_w, textvariable=var)
b1=Button(my_w,text="DATA ACQUISITION",command=lambda: dataAcquisition(),height = 1, width = 30)
b1.grid(row=1,column=0)
b2=Button(my_w,text="DATA LOADER",command=lambda: dataLoader(),height = 1, width = 30)
b2.grid(row=2,column=0)
b3=Button(my_w,text="DATA EXPLORER",command=lambda:dataExplorer() ,height = 1, width = 30)
b3.grid(row=3,column=0)
b4=Button(my_w,text="DATA EVOLUTION ANALYZER",command=lambda: my_w.destroy(),height = 1, width = 30)
b4.grid(row=4,column=0)
my_w.mainloop()