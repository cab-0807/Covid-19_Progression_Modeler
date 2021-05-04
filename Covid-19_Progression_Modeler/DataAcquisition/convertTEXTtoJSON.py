import os
import search
import re
import json
from datetime import date, time, datetime
from tkinter import *
import tkinter.messagebox 
#------------------------------Main Function (récupération, correction des mots, ... Conversion vers JSON )--------------------------
def transformTEXToJSON(path):
    aujourdhui=date.today()
    #date__ 
    date__=""
    r=[]
    Data=date_(path)
    if(len(Data)>4): 
        if(Data[3].isnumeric()):
            Data[2]=Data[3]
            Data[3]=Data[4]
            Data[4]=Data[5]
        lesMois = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet','aout','septembre','octobre','novembre','décembre']
        a=","
        for char in a:
            Da= Data[4].split(",")
        for i in range(len(lesMois)-1):
            r=permuter(lesMois[i])#On cherche les anagrammes de la chaine
            for j in range(len(r)):#Si le mois (le mois n'est pas bien écrit), on cherhe s'il est dans un des anagrammes
                if(Data[3] in r[j]):
                    date__=Data[2]+'-'+str(i+1)+'-'+Da[0]
                    mois_l=lesMois[i]
    else:#Dans le cas où le fichier est incomplet
        Annee="null"
        mois_l="null"
        date__="null"

    #NbTest, Nb nouveaux Cas
    Data0=NbreTest_NvCas(path)
    if(len(Data0)<5):#Dans le cas où le fichier est incomplet
        Nbre_Test="null"
        Nbre_Nouveau_Cas="null"
    else:
        Nbre_Test=int(Data0[1])
        Nbre_Nouveau_Cas=int(Data0[4])
        
    #TauxPositivité
    Data1=Taux_Positivite(path)
    Taux_Pos=""
    if(len(Data1)<3):#Dans le cas où le fichier est incomplet
        Taux_Pos=0000
    else:
        if(len(Data1)<10):
            for i in range(len(Data1)):
                a=","
                Taux_temp=""
                for char in a:
                    Data1[i]= Data1[i].replace(char,"")
            for i in range(len(Data1)):
                Taux_Pos=Data1[i]
                for j in range(len(Taux_Pos)):
                    if(Taux_Pos[j].isnumeric()):
                        Taux_temp=Taux_temp+Taux_Pos[j]
                    else:
                        pass
                str(Taux_temp)
            Taux_Pos=Taux_temp[0]+"."+Taux_temp[1:3]
            Taux_Pos=float(Taux_Pos)
        else:
            for i in range(len(Data1)):
                a=","
                Taux_temp=""
                for char in a:
                    Data1[i]= Data1[i].replace(char,"")
            for i in range(len(Data1)):
                Taux_Pos=Data1[i]
                for j in range(len(Taux_Pos)):
                    if(Taux_Pos[j].isnumeric()):
                        Taux_temp=Taux_temp+Taux_Pos[j]
                    else:
                        pass
                str(Taux_temp)
            Taux_Pos=Taux_temp[0]+"."+Taux_temp[1:3]
            Taux_Pos=float(Taux_Pos)

    #CasContact
    Data2=Nbre_Cas_Contact(path)
    if(len(Data2)<2):#Dans le cas où le fichier est incomplet
        Nbre_CasContacts=0000
    else:
        if(isinstance(Data2[0], int)):
            Nbre_CasContacts=Data2[0]
        else:
            Nbre_CasContacts=Data2[1]
    
    #CasCommunautaire
    Data3=Nbre_Cas_Communautaire(path)
    if(len(Data3)<2):#Dans le cas où le fichier est incomplet
        Nbre_CasCommunautaires=0000
    else:
        if(isinstance(Data3[0], int)):
            Nbre_CasCommunautaires=Data3[0]
        elif(isinstance(Data3[1], int)):
            Nbre_CasCommunautaires=Data3[1]
        else:
            Nbre_CasCommunautaires=Data3[0]

    #NbGuéris
    Data4=Nbre_Cas_Gueris(path)
    if(len(Data4)<11):#Dans le cas où le fichier est incomplet
        Nbre_Gueris=0000
    else:
        Nbre_Gueris=int(Data4[10])

    #NbDécès
    Data5=NbreDeces(path)
    if(len(Data4)<2):#Dans le cas où le fichier est incomplet
        Nbre_Deces=0000
    else:
        Nbre_Deces=int(Data5[1])

    #LesLocalités
    Dakar=Dakar_(path) #Récupération de la liste des localités de Dakar
    Dakar=list(filter(None, Dakar)) #Suppression des lignes vides
    region=Regions(path)#Récupération de la liste des régions
    region=list(filter(None, region))
    if(len(Dakar)!=0 and len(region)!=0):
                    #Correction Ecriture des régions
        for i in range(len(region)):
            if(isinstance(region[i],int)==False):
                region[i]=region[i].replace("\n","")#Suppression des sauts de ligne
                region[i]=region[i].lower()#Mettre les élèments de la liste en miniscule
                a="é,è"
                for word in a :
                    region[i]=region[i].replace(word,"e")#Suppression des accents
            region[i]=search.search_(region[i])#Correction des erreurs  (niveau ecriture)
        number=0
        for i in range(len(region)):
            if(region[i]==" "):
                region[i]=region[i+1]#Suppression des lignes vides en dupliquant les lignes d'avant
        reg= [] #Création de notre liste finale (On y stocke nos données corrigées)
        for i in range(len(region)):
            if(isinstance(region[i],int)):
                if(isinstance(region[i+1],str)):
                    number=region[i] #Nombre de cas
                else:
                    pass 
            else:
                reg.append([region[i],number]) #Stockage des régions avec leur nombre de cas
                    #Correction Ecriture des régions
        for i in range(len(Dakar)):
            if(isinstance(Dakar[i],int)==False):
                Dakar[i]=Dakar[i].replace("\n","")
                Dakar[i]=Dakar[i].lower()
                a="é,è"
                for word in a :
                    Dakar[i]=Dakar[i].replace(word,"e")
            Dakar[i]=search.search_(Dakar[i])
        number=0
        for i in range(len(Dakar)-1):
            if(Dakar[i]==" "):
                Dakar[i]=Dakar[i+1]
        reg_dkr= []
        for i in range(len(Dakar)-1):
            if(isinstance(Dakar[i],int)):
                if(isinstance(Dakar[i+1],str)):
                    number=Dakar[i]
                else:
                    pass 
            else:
                reg_dkr.append([Dakar[i],number])

        #--------------------------Enregistrement dans des fichiers texte----------------
        temporyNameOfFIle = path[:-3]
        temporyNameOfFIle1 = path[3:-12]
        temporyNameOfFIle =  temporyNameOfFIle.replace('_',"")
        temporyNameOfFIle =  temporyNameOfFIle.replace('-',"")
          #Enregistrement des données
        with open('DataTxtFiles/data_donnees'+temporyNameOfFIle+'txt','w') as file:
            file.write("id_com %s\n" %temporyNameOfFIle1)
            file.write("date__ %s\n" %date__)
            file.write("nb_test %s\n" %str(Nbre_Test))
            file.write("nb_nv_cas %s\n" %str(Nbre_Nouveau_Cas))
            file.write("nb_cas_contact %s\n" %str(Nbre_CasContacts))
            file.write("nb_cas_communautaire %s\n" %str(Nbre_CasCommunautaires))
            file.write("nb_gueris %s\n" %str(Nbre_Gueris))
            file.write("nb_deces %s\n" %str(Nbre_Deces))
            file.write("date___heure_extraction %s\n" %aujourdhui)
        file.close()          
                    #Enregistrement des régions
        with open('DataTxtFiles/data'+temporyNameOfFIle+'txt','a') as file:
            for i in range(0,len(reg)):
                temp=reg[i]
                for j in range(0,len(temp)-1):
                    entree=temp[j].upper()+" "+str(temp[j+1])
                    file.write("%s\n" %entree)
        file.close()
                    #Enregistrement des localités de Dakar
        with open('DataTxtFiles/data_dkr'+temporyNameOfFIle+'txt','a') as file:
            for i in range(0,len(reg_dkr)):
                temp=reg_dkr[i]
                for j in range(0,len(temp)-1):
                    entree=temp[j].upper()+" "+str(temp[j+1])
                    if(len(entree)>6):
                        file.write("%s\n" %entree)
        file.close()

        #Conversion vers JSON
                  #----------------------Les données--------------------------------
        if(os.path.exists("JSONFiles/"+mois_l.upper()+".json")):
            filename_js = 'JSONFiles/'+mois_l.upper()+'.json'
            filename = 'DataTxtFiles/data_donnees'+temporyNameOfFIle+'txt'
            # creation of dictionaries
            dict1 = {}
            dict3= {}
            dict2= {}
            Liste_donnees=[]
            fields =['id_com', 'date','nb_test','nb_nv_cas','nb_cas_contact','nb_cas_communautaire','nb_gueris','nb_deces','date_heure_extraction']
            if(os.path.getsize(filename_js)==0):#Si fichier json vide
                with open(filename) as fh:
                    myline = fh.readlines() #On parcours tout le fichier 
                    length=len(myline)#Taille du fichier
                    i=0
                    for line in myline:
                            # reading line by line from the text file
                        description = list( line.strip().split(None, 2))
                        description_=' '.join(description)
                        if(length>1):
                                Liste_donnees.append(description_.split(" ")[1])
                    while i<len(Liste_donnees):
                        dict2[fields[i]]= Liste_donnees[i]
                        i = i + 1
                    dict3[date__]=dict2
                    fh.close()
                    # creating json file        
                out_file = open('JSONFiles/'+mois_l.upper()+'_temp.json', "w")# file open in adding mode
                json.dump(dict3, out_file, indent = 4) # Adding 
                out_file.close()
            else:
                with open(filename_js) as foo:
                    data=json.load(foo)
                    with open(filename) as fh:
                        myline = fh.readlines() #On parcours tout le fichier 
                        length=len(myline)#Taille du fichier
                        i=0
                        for line in myline:
                                # reading line by line from the text file
                            description = list( line.strip().split(None, 2))
                            description_=' '.join(description)
                            if(length>1):
                                    Liste_donnees.append(description_.split(" ")[1])
                        while i<len(Liste_donnees):
                            dict2[fields[i]]= Liste_donnees[i]
                            i = i + 1
                        dict3[date__]=dict2
                        data.update(dict3)
                        fh.close()
                    foo.close()
                    # creating json file        
                out_file = open('JSONFiles/'+mois_l.upper()+'_temp.json', "w")# file open in adding mode
                json.dump(data, out_file, indent = 4) # Adding 
                out_file.close()
        #----------------------Régions--------------------------------
        if(os.path.exists("JSONFiles/"+mois_l.upper()+"_temp.json")):
            filename = 'JSONFiles/'+mois_l.upper()+'_temp.json'
            filename_ = 'DataTxtFiles/data'+temporyNameOfFIle+'txt'
            # creation of dictionnariesresultant dictionary
            dict1 = {}
            dict2= {}
            # fields in the sample file 
            with open(filename) as fh:
                data=json.load(fh)
                with open(filename_) as f:
                    for line in f:
                        description = list( line.strip().split(None, 2)) 
                        # loop variable
                        i = 0
                        dict2 = {}
                        while i<len(description):
                            sno =description[0]
                            if(len(description)>1):
                                dict2['NbreCas']= description[i][0]
                            i = i + 1
                        dict1[sno]=dict2
                    data[date__].update(dict1) #Adding the dictionary to the json file
                f.close() 
            out_file = open('JSONFiles/'+mois_l.upper()+'_temp.json', "w")
            json.dump(data, out_file, indent = 3)  
            out_file.close()
        
        #----------------------Dakar--------------------------------
        if(os.path.exists("JSONFiles/"+mois_l.upper()+"_temp.json")):
            filename = 'JSONFiles/'+mois_l.upper()+'_temp.json'
            filename_ = 'DataTxtFiles/data_dkr'+temporyNameOfFIle+'txt'
            # creation of dictionnariesresultant dictionary
            dict1 = {}
            dict3= {}
            # fields in the sample file 
            fields =['NomLocalite', 'NbreCas']
        
            with open(filename) as fh:
                data=json.load(fh)
                with open(filename_) as f:
                    for line in f:
                        # reading line by line from the text file
                        description = list( line.strip().split(None, 2)) 
                        # loop variable
                        i = 0
                        dict2 = {}
                        while i<len(description):
                            sno =description[0]
                            if(len(description)>1):
                                dict2['NbreCas']= description[i][0]
                            i = i + 1
                        dict1[sno]= dict2
                    dict3["DAKAR"]=dict1
                    data[date__].update(dict3) #Adding the dictionary to the json file
                f.close() 

                #----------------------Ajout des données pour chaque jour--------------------------------
            out_file = open('JSONFiles/'+mois_l.upper()+'.json', "w")
            json.dump(data, out_file, indent = 3)  
            out_file.close()
        print(     ">"+temporyNameOfFIle+"txt converted to "+temporyNameOfFIle+"json")
        os.system("rm JSONFiles/"+mois_l.upper()+"_temp.json")
        print("*****************************************************************************")
    else:
        pass



#------------------------------Récupération de la date__ au niveau du fichier texte--------------------------
def date_(path):
    temporyNameOfFIle = path[:-3]
    temporyNameOfFIle =  temporyNameOfFIle.replace('_',"")
    temporyNameOfFIle =  temporyNameOfFIle.replace('-',"")
    maListe = []
    if(os.path.exists('TextFiles/'+temporyNameOfFIle+'txt')):
        
        with open('TextFiles/'+temporyNameOfFIle+'txt','r') as file:
            myline = file.readlines()
            length=len(myline)
            cdc=myline[1]
            maListe = cdc.split(" ") # la fonction split sépare et enregistre chaque mot de notre cdc(la ligne 1) dans la liste maListe 

        file.close()
    else:
        print("Nous n'avons pas pu convertir le fichier pdf en fichier texte")
    return maListe

#------------Récupération du nombre de Tests et du nombre de nouveaux cas  au niveau du fichier texte--------------
def NbreTest_NvCas(path):
    maListe = []
    temporyNameOfFIle = path[:-3]
    temporyNameOfFIle =  temporyNameOfFIle.replace('_',"")
    temporyNameOfFIle =  temporyNameOfFIle.replace('-',"")
    if(os.path.exists('TextFiles/'+temporyNameOfFIle+'txt')):
        with open('TextFiles/'+temporyNameOfFIle+'txt','r') as file:
            myline = file.readlines()
            length=len(myline)
            for i in range(len(myline)):
                cdc=myline[i]
                if("tests" in cdc ):# On voit si "tests" est présent dans la ligne parcourue
                    temp=i #On garde le numéro de la ligne
                    maListe = cdc.split(" ") # la fonction split sépare et enregistre chaque mot de notre cdc dans la liste maListe 
                else:
                    pass     
        file.close()
    else:
        print("Nous n'avons pas pu convertir le fichier pdf en fichier texte")
    return maListe

#------------Récupération du taux de positivité--------------
def Taux_Positivite(path):
    Liste = []
    temporyNameOfFIle = path[:-3]
    temporyNameOfFIle =  temporyNameOfFIle.replace('_',"")
    temporyNameOfFIle =  temporyNameOfFIle.replace('-',"")
    if(os.path.exists('TextFiles/'+temporyNameOfFIle+'txt')):
        with open('TextFiles/'+temporyNameOfFIle+'txt','r') as file:
            myline = file.readlines()
            length=len(myline)
            for i in range(len(myline)):
                cdc=myline[i]
                if("tests" in cdc ):
                    if("taux de positiité" in cdc):
                        cdc=myline[temp+1]
                        Liste = cdc.split(" ") 
                    else:
                        temp=i
                        cdc=myline[temp+1]
                        Liste = cdc.split(" ") # la fonction split sépare et enregistre chaque mot de notre cdc dans la liste maListe 
                else:
                    pass  
        file.close()
    else:
        print("Nous n'avons pas pu convertir le fichier pdf en fichier texte")
    return Liste

#------------Récupération du nomre de cas contact--------------
def Nbre_Cas_Contact(path):
    Liste = []
    temporyNameOfFIle = path[:-3]
    temporyNameOfFIle =  temporyNameOfFIle.replace('_',"")
    temporyNameOfFIle =  temporyNameOfFIle.replace('-',"")
    if(os.path.exists('TextFiles/'+temporyNameOfFIle+'txt')):
        with open('TextFiles/'+temporyNameOfFIle+'txt','r') as file:
            myline = file.readlines()
            length=len(myline)
            for i in range(len(myline)):
                cdc=myline[i]
                if("Cas contacts" in cdc ):
                    Liste = cdc.split(" ") # la fonction split sépare et enregistre chaque mot de notre cdc dans la liste maListe 
                else:
                    pass  
        file.close()
    else:
        print("Nous n'avons pas pu convertir le fichier pdf en fichier texte")
    return Liste

#------------Récupération du nombre de cas communautaires--------------
def Nbre_Cas_Communautaire(path):
    Liste = []
    temporyNameOfFIle = path[:-3]
    temporyNameOfFIle =  temporyNameOfFIle.replace('_',"")
    temporyNameOfFIle =  temporyNameOfFIle.replace('-',"")
    if(os.path.exists('TextFiles/'+temporyNameOfFIle+'txt')):
        Liste = []
        with open('TextFiles/'+temporyNameOfFIle+'txt','r') as file:
            myline = file.readlines()
            length=len(myline)
            for i in range(len(myline)):
                cdc=myline[i]
                if("cas issus de la transmission communautaire" in cdc ):
                    Liste = []
                    Liste = cdc.split(" ") # la fonction split sépare et enregistre chaque mot de notre cdc dans la liste maListe 
                else:
                    pass  
        file.close()
    else:
        print("Nous n'avons pas pu convertir le fichier pdf en fichier texte")
    return Liste

#------------Récupération du nombre de guéris--------------
def Nbre_Cas_Gueris(path):
    Liste = []
    temporyNameOfFIle = path[:-3]
    temporyNameOfFIle =  temporyNameOfFIle.replace('_',"")
    temporyNameOfFIle =  temporyNameOfFIle.replace('-',"")
    if(os.path.exists('TextFiles/'+temporyNameOfFIle+'txt')):
        Liste = []
        with open('TextFiles/'+temporyNameOfFIle+'txt','r') as file:
            myline = file.readlines()
            length=len(myline)
            for i in range(len(myline)):
                cdc=myline[i]
                if("A ce jour" in cdc ):
                    Liste = []
                    Liste = cdc.split(" ") # la fonction split sépare et enregistre chaque mot de notre cdc dans la liste maListe 
                else:
                    pass  
        file.close()
    else:
        print("Nous n'avons pas pu convertir le fichier pdf en fichier texte")
    return Liste

#------------Récupération du nombre de décès--------------
def NbreDeces(path):
    Liste = []
    temporyNameOfFIle = path[:-3]
    temporyNameOfFIle =  temporyNameOfFIle.replace('_',"")
    temporyNameOfFIle =  temporyNameOfFIle.replace('-',"")
    if(os.path.exists('TextFiles/'+temporyNameOfFIle+'txt')):
        with open('TextFiles/'+temporyNameOfFIle+'txt','r') as file:
            myline = file.readlines()
            length=len(myline)
            for i in range(len(myline)):
                cdc=myline[i]
                if("décédés" in cdc ):
                    Liste = []
                    Liste = cdc.split(" ") # la fonction split sépare et enregistre chaque mot de notre cdc dans la liste maListe 
                else:
                    pass  
        file.close()
    else:
        print("Nous n'avons pas pu convertir le fichier pdf en fichier texte")
    return Liste
#--------------------------Récupération des données pour Dakar (Localités et nombre de cas--------------
def Dakar_(path):
    Liste = []
    sortie=[]
    temporyNameOfFIle = path[:-3]
    temporyNameOfFIle =  temporyNameOfFIle.replace('_',"")
    temporyNameOfFIle =  temporyNameOfFIle.replace('-',"") 
    if(os.path.exists('TextFiles/'+temporyNameOfFIle+'txt')):
        #Crétion de liste
        with open('TextFiles/'+temporyNameOfFIle+'txt','r') as file:
            myline = file.readlines() #On parcours tout le fichier 
            length=len(myline)#Taille du fichier
            #print(length)
            if(length>=30): #30 est la taille minimale pour pouvoir prendre nos données
                for i in range(len(myline)):
                    cdc=myline[i]
                    if("comme suit" in cdc ):
                        debut=i+2 #Valeur de début pour notre recherche (2 lignes après avoir vu "comme suit")
                for j in range(len(myline)):
                    cdc=myline[j]
                    if("Régions" in cdc):
                        fin=j#Valeur de fin pour notre recherche (après avoir vu "Régions")

                for j in range(debut,fin,1):
                    cdc=myline[j]
                    Liste = cdc.split(" ") # la fonction split sépare et enregistre chaque mot de notre cdc dans la liste maListe 
                    #---------Autre nettoyage des valeurs à stocker dans la liste et suppression des valeurs indésirables---------
                    for i in range(len(Liste)-1):
                        Liste[i]= Liste[i].strip(',')
                        b="O,0"
                        for char in b:
                            Liste[i]= Liste[i].replace(char,"")
                        Liste[i].strip('et')
                        if(Liste[i]=="aux"  or Liste[i]==";" or Liste[i]=="-" ):
                            Liste[i]=" "
                        if(Liste[i]=="a"  or Liste[i]=="et" or Liste[i]=="la" or Liste[i]=="au"):
                            Liste[i]=" "
                    Liste = [i for i in Liste if not i.isspace()] #Suppression des espaces dans la liste
                    
                    for i in range(len(Liste)-1):
                        if(Liste[i].isnumeric()):
                            if( Liste[i-1].isnumeric() and isinstance(Liste[i+1], str)  ):
                                Liste[i]=""
                        if(Liste[i].isnumeric()):
                            if( Liste[i-1].isnumeric() and isinstance(Liste[i+1], str)  ):
                                Liste[i]=""

                    for j in range(len(Liste)):
                        specialCharacter =  '''!()[]{};:'"\<>./?@#$%^&*_~v¥V'''
                    if(Liste[j].isnumeric()==False):
                        for char in specialCharacter:
                            Liste[j]= Liste[j].replace(char,"")
                    Liste = [i for i in Liste if not i.isspace()]
                    #--------------------------------------------------------------------

                    for i in range(len(Liste)-1):
                            if(Liste[i].isnumeric()):
                                Liste[i]=int(Liste[i])#Convertir les valeurs numériques en entier
                    sortie=sortie+Liste
            else:
                tkinter.messagebox.showinfo("Alert","Le fichier texte obtenu est incomplet, nous ne pouvons pas extraire toutes les données.") 
                print("Le fichier est incomplet, nous ne pouvons pas extraire tous les données que nous avons besoin")#Si la taille du fichier est inférieur à la taille minimale pour extraire nos données
        file.close()
    else:
        print("Nous n'avons pas pu convertir le fichier pdf en fichier texte")
    return sortie

#--------------------------Récupération des données pour les régions --------------
def Regions(path):
    Liste = []
    sortie= []
    pos=[]
    region=[]
    temporyNameOfFIle = path[:-3]
    temporyNameOfFIle =  temporyNameOfFIle.replace('_',"")
    temporyNameOfFIle =  temporyNameOfFIle.replace('-',"")
    if(os.path.exists('TextFiles/'+temporyNameOfFIle+'txt')):
        #Crétion de liste
        #*******Pour bien comprendre, veuillez voir la fonction précédente
        with open('TextFiles/'+temporyNameOfFIle+'txt','r') as file:
            myline = file.readlines()
            length=len(myline)
            if(length>=30):
                for i in range(len(myline)):
                    cdc=myline[i]
                    if("Régions" in cdc ):
                        debut=i+1
                for j in range(len(myline)):
                    cdc=myline[j]
                    if("patients suiis" in cdc):
                        fin=j

                for j in range(debut,fin,1):
                    cdc=myline[j]
                    Liste = cdc.split(" ") # la fonction split sépare et enregistre chaque mot de notre cdc dans la liste maListe 
                    for i in range(len(Liste)-1):
                        b="O"
                        for char in b:
                            temp= Liste[i].replace(char,"0")
                            Liste[i]=temp
                        if(Liste[i]=="aux" or Liste[i]=="et" or Liste[i]=="e" or Liste[i]=="," or Liste[i]=="a" or Liste[i]=="-"):
                            Liste[i]=" "
                        if((Liste[i].isnumeric() and Liste[i+1].isnumeric()) ):
                            Liste[i+1]=" "
                        a=","
                        for char in a:
                            Liste[i]= Liste[i].replace(char,"")
                    Liste = [i for i in Liste if not i.isspace()]

                    for i in range(len(Liste)-1):
                        if(isinstance(Liste[i], int)):
                            if( Liste[i-1]!="-" and isinstance(Liste[i-1], str) and isinstance(Liste[i+1], str)==False  ):
                                Liste[i]=""
                    for j in range(len(Liste)):
                        specialCharacter =  '''!()[]{};:'"\<>./?@#$%^&*_~v¥V'''
                        if(Liste[j].isnumeric()==False):
                            for char in specialCharacter:
                                Liste[j]= Liste[j].replace(char,"")
                    Liste = [i for i in Liste if not i.isspace()]
                    for i in range(len(Liste)-1):
                        if(Liste[i].isnumeric()):
                            Liste[i]=int(Liste[i])
                        else:
                            Liste[i]=str(Liste[i])
                    sortie=sortie+Liste
            else:
                print("Le fichier est incomplet, nous ne pouvons pas extraire tous les données que nous avons besoin")
        file.close()
    else:
        print("Nous n'avons pas pu convertir le fichier pdf en fichier texte")
    return sortie

#--------------------------Fontion pour trouver les anagrammes --------------
def permuter(items):
    if len(items) <= 1:
        return [items]
    liste=[]
    for p in permuter(items[1:]):
        for i in range(len(items)):
            liste.append(p[:i]+items[0:1]+p[i:])
    return liste

        	