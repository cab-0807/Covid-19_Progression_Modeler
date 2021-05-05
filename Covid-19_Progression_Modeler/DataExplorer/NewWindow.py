from tkinter import *
from tkinter import messagebox
import tkinter.messagebox
import sys
import mysql.connector
import os
import matplotlib.pyplot as plt

identifiants__=[]
Liste_Dates=[]

if(os.path.getsize("../DataLoader/temp.txt")!=0):
    with open('../DataLoader/temp.txt','r') as file:
        myline = file.readlines()
        for line in myline:
            identifiants = list( line.strip().split(None, 2))
            identifiants_=''.join(identifiants)
            identifiants__.append(identifiants_)
    file.close()
    user=identifiants__[0]
    password=identifiants__[1]
    #Connectinng to the DB
    con = mysql.connector.connect(
                user=user, 
                password=password,
                host='127.0.0.1',
                database='DataLoader')
    curseur= con.cursor()
#Rechercher le nombbre de cas de la région
request = "SELECT Nbre_Cas from Regions WHERE NomRegion="+"'"+sys.argv[1]+"'"+""
curseur.execute(request)
Nbre_Cas=curseur.fetchone()
print(Nbre_Cas[0])

def details():
    x=[]
    y=[]

    request = "SELECT date from Communiques "
    curseur.execute(request)
    Dates=curseur.fetchall()
    for i in range(len(Dates)):
        if(sys.argv[1]=="DAKAR"):
            request1 = "SELECT SUM(Nbre_Cas) from "+"`"+Dates[i][0]+"`"+" where Localites LIKE 'DAKAR_%'"
            curseur.execute(request1)
            Nbre_Cas=curseur.fetchone()
            #print(Nbre_Cas[0])
            y.append(Dates[i][0])
            x.append(Nbre_Cas)
        else:
            Loc=[]
            print(Dates[i][0])
            request0 = "SELECT Localites from "+"`"+Dates[i][0]+"`"+""
            curseur.execute(request0)
            Localites=curseur.fetchall()
            for p in enumerate(Localites):
                print(p[1][0])
                Loc.append(p[1][0])
            if (sys.argv[1] in Loc) :
                print("in")
                request1 = "SELECT Nbre_Cas from "+"`"+Dates[i][0]+"`"+" where Localites='"+""+sys.argv[1]+""+"'"
                curseur.execute(request1)
                Nbre_Cas=curseur.fetchone()
                y.append(Dates[i][0])
                x.append(Nbre_Cas)
            else: 
                print("not in")
        print(Liste_Dates)
    plt.title("Courbe temporelle d'évolution de: "+sys.argv[1])
    print(x)
    print(y)
    plt.plot(x,y,color='green',linestyle='dashed',linewidth=3,marker='o',markerfacecolor='blue',markersize=12)
    plt.xlabel('Vitesse')
    plt.ylabel('Temps')
    plt.show()

fenetre = Tk()

fenetre.title(sys.argv[1])
fenetre.geometry("110x90")

N_total=0

var = StringVar()
lbl = Label(fenetre, textvariable=var)
request = "SELECT date from Communiques "
curseur.execute(request)
Dates=curseur.fetchall()
for i in range(len(Dates)):
    if(sys.argv[1]=="DAKAR"):
        request1 = "SELECT SUM(Nbre_Cas) from "+"`"+Dates[i][0]+"`"+" where Localites LIKE 'DAKAR_%'"
        curseur.execute(request1)
        Nbre_Cas=curseur.fetchone()
        #print(Nbre_Cas[0])

var.set(""+ sys.argv[1]+"\n Nbre de cas: "+str(Nbre_Cas[0])+"")
lbl.grid(row=0, column=1)
b2=Button(fenetre,text="Détails",command=lambda: details())
b2.grid(row=1,column=1)
fenetre.mainloop()
