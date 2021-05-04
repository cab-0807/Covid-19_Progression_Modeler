import os
import pandas as pd
import numpy as np
import tweepy
from tweepy import OAuthHandler
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse
from requests_oauthlib import OAuth1
from datetime import date, time, datetime
import pytesseract
from tkinter import *
from tkinter import messagebox
import convertPDFtoTEXT
import convertTEXTtoJSON


def downloadFile(url):
    # Recuperation du nom du fichier à travers un slicing
    temporyNameOfFIle = url[40:]
    temporyNameOfFIle_ = url[43:-12]
    print(     "> Downloading")
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
        'AppleWebKit/537.11 (KHTML, like Gecko) '
        'Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'
    }
    #Passage de l'URL du fichier
    try:
        request = requests.get(url, headers=headers)
        if(request.status_code == 200): #La requete s'est bien executée et la ressource a ete bien recupéree
            with open('PdfFiles/'+temporyNameOfFIle, 'wb') as file:  #Ouverture d'un fichier 
            # Ecriture du contenu 
                file.write(request.content)
            file.close()
            messagebox.showinfo("Alert","The communique "+temporyNameOfFIle_+" has been downloaded as PDF") 
        else:
            pass
    except:
        pass
   #------------------------------Fonctions Fenêtre pour demannder le choix--------------------------
def touche_entree(event):
    """Même chose qu'un clic sur le bouton de soumission ou sur terminer quand soumission faite."""
    if bouton_terminer.winfo_viewable():
        fenetre.destroy()
    else:
        soumettre_click()

def ok():
    b1.grid_forget()
    b2.grid(row=1,column=0)
    b3.grid(row=2,column=0)
    b4.grid(row=3,column=0)

def first():
        #Handle Twitter API authentication
    consumer_key= 'VTkyPviL3fFF8xcsJ7wQt49qb'
    consumer_secret= 'pwioBaARTxb9zXRzwDNPQZdj7q3gQTMeBGtACqoeYXiQG1sQud'
    access_token= '716396574293823489-p7N37x3MCvLVhLIU2tBXZSiHQjUs7LF'
    access_token_secret= 'T81V5hNvO97d8MCE0uY558VhdOoxOch4Ij9NTL8YsuFnR'
    
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    api = tweepy.API(auth)
    #------------------------------Récupération du numéro du communiqué du jour avec tweepy--------------------------
    # Créer une instance de l'objet date.
    aujourdhui=date.today()

    jour=aujourdhui.day
    mois=aujourdhui.month
    annee=aujourdhui.year
    leJour = aujourdhui.weekday()

    lesJours = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']
    lesMois = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet','aout','septembre','octobre','novembre','décembre']
    Jour=lesJours[leJour]
    Moi=lesMois[mois-1]

    #pull tweets from specific user. In userID, just put the page's username
    userID = "MinisteredelaS1"
    tweets = api.user_timeline(screen_name=userID, 
        count=2,
        include_rts = False,
        since=""+str(annee)+"-"+str(mois-1)+"-"+str(leJour)+"",
        until=""+str(annee)+"-"+str(mois-1)+"-"+str(leJour-1)+"")

    #------------------------------Récupération du numéro du communiqué du jour avec tweepy--------------------------
    for tweet in tweets[:4]:#On prend les deux derniers tweets du jour
        x=tweet.text
        if "Communiqué" in x:
            i=x[11:14] #On sort le numéro du communiqué
    #------------------------------Création des fichiers json--------------------------
    lesMois = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet','aout','septembre','octobre','novembre','décembre']
    for j in range(len(lesMois)):
        if(os.path.exists("JSONFiles/"+lesMois[j].upper()+".json")):
            pass
        else:
            os.system("touch JSONFiles/"+lesMois[j].upper()+".json")

    #------------------------------Téléchargement ET Conversion--------------------------
    url = 'https://sante.sec.gouv.sn/sites/default/com'
    extension = '_covid19.pdf'
    print(     ">Looking For Communique Number: "+i)
    try:
        downloadFile(url+(i)+extension)
        convertPDFtoTEXT.transformPDFToText("com"+(i)+extension)
    except:
        try:
            downloadFile(url+(i)+extension)
            convertPDFtoTEXT.transformPDFToText("com"+(i)+extension)
        except:
            try:
                downloadFile(url+(i)+extension)
                convertPDFtoTEXT.transformPDFToText("com"+(i)+extension)
            except:
                pass

    convertTEXTtoJSON.transformTEXToJSON("com"+(i)+extension)


def on_change(e):
    i=str(e.widget.get())
    print (e.widget.get())
    e.widget.config(state='disabled')
    if(i.isnumeric()):
            #------------------------------Création des fichiers json--------------------------
        lesMois = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet','aout','septembre','octobre','novembre','décembre']
        for j in range(len(lesMois)):
            if(os.path.exists("JSONFiles/"+lesMois[j].upper()+".json")):
                pass
            else:
                os.system("touch JSONFiles/"+lesMois[j].upper()+".json")

        #------------------------------Téléchargement ET Conversion--------------------------
        url = 'https://sante.sec.gouv.sn/sites/default/com'
        extension = '_covid19.pdf'
        print(     ">Looking For Communique Number: "+i)
        downloadFile(url+(i)+extension)
        convertPDFtoTEXT.transformPDFToText("com"+(i)+extension)
        convertTEXTtoJSON.transformTEXToJSON("com"+(i)+extension)
    else:
        messagebox.showinfo("Alert","You had to give a number") 


def second():
    root = Tk()
    root.title("Give a number")
    e = Entry(root)
    e.pack()    
    # Calling on_change when you press the return key
    e.bind("<Return>", on_change)  
    

    root.mainloop()
def on_change1(e):
    interval=str(e.widget.get())
    if "-" in interval:
        start="".join(interval.split("-")[0])
        end="".join(interval.split("-")[1])
        if(start.isnumeric() and end.isnumeric() ):
            start=int(start)
            end=int(end)
                #------------------------------Création des fichiers json--------------------------
            lesMois = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet','aout','septembre','octobre','novembre','décembre']
            for j in range(len(lesMois)):
                if(os.path.exists("JSONFiles/"+lesMois[j].upper()+".json")):
                    pass
                else:
                    os.system("touch JSONFiles/"+lesMois[j].upper()+".json")
            #------------------------------Téléchargement ET Conversion--------------------------
            url = 'https://sante.sec.gouv.sn/sites/default/com'
            extension = '_covid19.pdf'
            for i in range(start,end):
                i=str(i)
                print(     ">Looking For communique number: "+i)
                try:
                    downloadFile(url+(i)+extension)
                    convertPDFtoTEXT.transformPDFToText("com"+(i)+extension)
                except:
                    try:
                        downloadFile(url+(i)+extension)
                        convertPDFtoTEXT.transformPDFToText("com"+(i)+extension)
                    except:
                        try:
                            downloadFile(url+(i)+extension)
                            convertPDFtoTEXT.transformPDFToText("com"+(i)+extension)
                        except:
                            pass
                convertTEXTtoJSON.transformTEXToJSON("com"+(i)+extension)
        else:
            print("Numbers!!!")
            messagebox.showinfo("Alert","You had to give an interval as specified \n Must have numbers from either side of "+'"''-''"'+"") 

    else:
        print("no -")
        messagebox.showinfo("Alert","You had to give an interval as specified \n There is no "+'"''-''"'+"") 
    e.widget.config(state='disabled')
    
def third():
    root = Tk()
    root.title("Give an interval")
    e = Entry(root)
    e.pack()    
    # Calling on_change when you press the return key
    e.bind("<Return>", on_change1)  
    
    root.mainloop()


 #------------------------------Fenêtre pour demannder le choix--------------------------
my_w=Tk()
my_w.title("DATA ACQUISITION")
my_w.geometry("307x160")
var = StringVar()
lbl = Label(my_w, textvariable=var)
messagebox.showinfo("Alert","Utilisant les sources de données officielles du Ministère de la Santé, ce module permettra de : \n \n • télécharger des fichiers pdfs et/ou des images des communiqués officiels du ministère de la santé dans un répertoire local \n \n • parcourir , extraire et agréger au fur et à mesure des téléchargements des fichiers, les données qu’elles contiennent pour les stocker dans des JSON") 
var.set("You have 3 choices:\n - Download Today's communique \n - Give the communique number to download \n - Give an interval" )
lbl.grid(row=0, column=0)
b1=Button(my_w,text="Ok",command=lambda: ok())
b1.grid(row=1,column=0)
b2=Button(my_w,text="Download Today's communique",command=first,height = 1, width = 30)
b3=Button(my_w,text="Give the communique number to download",command=second,height = 1, width = 30)
b4=Button(my_w,text="Give an interval",command=third,height = 1, width = 30)

my_w.mainloop()




