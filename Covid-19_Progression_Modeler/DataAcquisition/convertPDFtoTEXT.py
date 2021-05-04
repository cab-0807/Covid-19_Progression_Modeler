import pdf2image
from PIL import Image
import pytesseract
import os
import requests
import fileinput

#------------------------------Main Function--------------------------
def transformPDFToText(path):
    temporyNameOfFIle = path[:-3]
    temporyNameOfFIle_ = path[:-4]
    temporyNameOfFIle =  temporyNameOfFIle.replace('_',"")
    temporyNameOfFIle =  temporyNameOfFIle.replace('-',"")

    pages = pdf2image.convert_from_path('PdfFiles/'+path, 200) #Conversion du pdf en image
    #Creation du fichier texte en y copiant le contenu des pdf apres leur transformation en image 
    with open('TextFiles/'+temporyNameOfFIle+'txt', 'wt') as file:
        for index, page in enumerate(pages):
            nameOfImage = temporyNameOfFIle+'_'+str(index)+'jpg'
            page.save(nameOfImage, 'JPEG')
            text = pytesseract.image_to_string(Image.open(nameOfImage))
            text = cleanText(text) #Nettoyage du texte
            file.write(text)
            os.remove(nameOfImage) #Suppresion de l'image apres l'ecriture de son contenu dans le fichier texte
    file.close()

    mon_fichier="TextFiles/"+temporyNameOfFIle+"txt"
    #os.remove(path) #Suppression du fichier pdf initial [à decommenter apres les tests]
    os.system("grep '\S' "+mon_fichier+">TextFiles/temp_"+temporyNameOfFIle+"txt")#Suppressio des espaces
    temp=0
    length=0
    with open('TextFiles/temp_'+temporyNameOfFIle+'txt', 'r') as file: #Ouverture du ficier en mode lecture
        myline = file.readlines() #Parcours du fichier ligne par ligne
        length=len(myline)
        for i in range(len(myline)):
            line=myline[i] #Parcours de ligne mot par mot
            if("COMMUNIQUE" in line ):#Voir si COMMUNIQUE est présent au niveau de la ligne, pour après les lignes précédents
                temp=i
            else:
                pass
    file.close()
    liste=[] #Création d'une liste
    with open('TextFiles/temp_'+temporyNameOfFIle+'txt', 'r') as file:#Ouverture du ficier en mode lecture
        myline = file.readlines()#Parcours du fichier ligne par ligne
        for j in range(temp,length,1):#Parcours du texte à partir de la ligne contenant COMMUNIQUE 
            element=myline[j] #On stocke chaque mot de la ligne dans element
            liste.append(element)#On ajoute l'élèment à la liste
    file.close()

    with open('TextFiles/temp_'+temporyNameOfFIle+'txt', 'w') as file:#Ouverture du ficier en mode écriture
        for j in range(len(liste)):#Parcours de la liste créée
            file.write(liste[j])#Ajout des élèments de la liste dans le fichier ouvert
    file.close()
    
    os.rename('TextFiles/temp_'+temporyNameOfFIle+'txt', 'TextFiles/'+temporyNameOfFIle+'txt')#Renommage du fichier en supprimant le fichier intermédiare créé
    print(     ">"+temporyNameOfFIle+"pdf converted to "+temporyNameOfFIle+"txt")

    return 'TextFiles/'+temporyNameOfFIle+'txt' 

def cleanText(text):
    #Nettoyage du texte pour éliminer les caractères spéciaux
    specialCharacter =  '''!()[]{};:'"\<>./?@#$%^&*_©°~v¥V'''
    
    text = str(text)
    for word in text:
        if word in specialCharacter:
            text = text.replace(word,"") 
    return text

