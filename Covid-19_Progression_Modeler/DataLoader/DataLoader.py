import mysql.connector, os, json
from tkinter import *
from tkinter import messagebox
import tkinter.messagebox
#Vérifying Identifiers, using Tkinter to ask for identifiers
def soumettre_click():
    """Ajoute le user dans le libellé puis affiche le libellé et le bouton pour terminer."""
    usr=str(user.get())
    pwd=str(password.get()) 
    bouton_soumission.grid_forget()
    user.configure(state=DISABLED)
    password.configure(state=DISABLED)
    with open('temp.txt','w') as file:
        file.write("%s\n" %usr)
        file.write("%s\n" %pwd)
    file.close()
    os.system("mysql -u "+usr+" --password="+pwd+" < DataLoader.sql")

    try:
        con = mysql.connector.connect(
            user=usr, 
            password=pwd,
            host='127.0.0.1',
            database='DataLoader')
        bouton_terminer.grid(row=3, columnspan=2, padx=5, pady=(5, 15))
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        messagebox.showinfo("", "Utilisateur ou Mot de passe \n incorrect\nSomething went wrong: {} ".format(err))
        bouton_terminer_error.grid(row=3, columnspan=2, padx=5, pady=(5, 15))

def done_click(): 
    fenetre.destroy()
    os.system("python3 DataLoader.py")

def touche_entree(event):
    """Même chose qu'un clic sur le bouton de soumission ou sur terminer quand soumission faite."""
    if bouton_terminer.winfo_viewable():
        fenetre.destroy()
    else:
        soumettre_click()
        
# fenêtre principale
fenetre = Tk()
fenetre.title('DATA LOADER')
messagebox.showinfo("Alert","Ce module permet le chargement des données téléchargées vers un serveur de base de données relationnelles en ligne") 
fenetre.bind("<Return>", touche_entree) # bouton par défaut
 
# libellé
libelle = Label(fenetre, text='Give us your MySQL user')
libelle.grid(row=0, column=0, sticky=E, padx=10, pady=10)
 
# zone de saisie
user = Entry(fenetre, width=30)
user.focus_set() # boîte de saisie par défaut
user.grid(row=0, column=1, padx=(0, 15), pady=10)

# libellé1
libelle1 = Label(fenetre, text='Give us your MySQL password')
libelle1.grid(row=1, column=0, sticky=E, padx=10, pady=10)
 
# zone de saisie
password = Entry(fenetre, width=30)
password.focus_set() # boîte de saisie par défaut
password.grid(row=1, column=1, padx=(0, 15), pady=10)

# bouton de soumission
bouton_soumission = Button(fenetre, text='Send', command=soumettre_click, padx=15)
bouton_soumission.grid(row=2, columnspan=2, padx=5, pady=(5, 15))
 
# bouton pour terminer le programme
bouton_terminer = Button(fenetre, text='Done', command=fenetre.destroy, padx=15)
bouton_terminer_error = Button(fenetre, text='Done', command=done_click, padx=15)
 
# la fenêtre s'affiche puis attend les interactions de l'usager
fenetre.mainloop()

#***********************************Adding Entries on DB****************************************
identifiants__=[]
os.system("touch temp.txt")
if(os.path.getsize("temp.txt")!=0):
    with open('temp.txt','r') as file:
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



def my_upd():
    line = l1.curselection()[0]
    item = l1.get(line)
    # on affecte la valeur de l'item à la variable :
    selected_date.set(item)
    idx = l1.get(0, END).index(item)
    l1.delete(idx)
    ListeDATE.remove(item)

def com():
    con.commit()
    my_w.destroy()
    
def rback():
    con.rollback()
    my_w.destroy()

    # read JSON files which is in JSONN folder
lesMois = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet','aout','septembre','octobre','novembre','décembre']
ListeDATE=[]

for MOIS in range(len(lesMois)):
    file = "../DataAcquisition/JSONFiles/"+lesMois[MOIS].upper()+".json"
    if(os.path.getsize(file)!=0):
        json_data=open(file).read()
        json_obj = json.loads(json_data)
        ListeNO={'id_com', 'date','nb_test','nb_nv_cas','nb_cas_contact','nb_cas_communautaire','nb_gueris','nb_deces','date_heure_extraction'}
        Liste=[]
        Liste_=[]
        
        for i, elt in enumerate(json_obj):
            ListeDATE.append(elt)
        # ***************Choisir les dates à enregistrer****************
        my_w=Tk()
        my_w.title(lesMois[MOIS].upper())
        l1=Listbox(my_w)
        l1.grid(row=1,column=0)
        # on crée une variable StringVar() pour stocker la
        # valeur de la date sélectionné pour supprimée
        selected_date = StringVar()

        for i in ListeDATE:
            l1.insert(END,i)
        b1=Button(my_w,text="Delete",command=lambda: my_upd())
        b1.grid(row=2,column=0)

        lbl = Label(my_w, textvariable=selected_date)
        lbl.grid(row=3, column=0)
        
        my_w.mainloop()
        for i, elt in enumerate(ListeDATE):
            #print(elt)
            request = "CREATE TABLE IF NOT EXISTS "+"`"+elt+"`"+" (""Localites varchar(50) NOT NULL PRIMARY KEY ,"" Nbre_Cas int(5) DEFAULT NULL"");"
            curseur.execute(request)
            for k in enumerate(json_obj[elt]):
                #print(k[1])
                if(k[1] not in ListeNO):
                    if(k[1]=="DAKAR" ):
                        for j in enumerate(json_obj[elt][k[1]]):
                            #print(j[1]) #Nom Localite
                            for o in enumerate(json_obj[elt][k[1]][j[1]]):
                                #print(o[1])
                                for n in enumerate(json_obj[elt][k[1]][j[1]][o[1]]):
                                    #print(n[1]) #Nbre de cas
                                    request1 = "SELECT Localites from "+"`"+elt+"`"+" "
                                    curseur.execute(request1)
                                    Regin=curseur.fetchall()
                                    if(len(Regin)!=0):
                                        for i in Regin:
                                            if("DAKAR_"+j[1]==i[0]):
                                                #print("Dans la base")
                                                request3 = "UPDATE "+"`"+elt+"`"+" SET Nbre_Cas=Nbre_Cas+"+str(int(n[1]))+" WHERE Localites="+"'"+i[0]+"'"+""
                                                #print(request3)
                                                curseur.execute(request3)
                                            else:
                                                #print(" Pas dans la base")
                                                request2 = "INSERT IGNORE INTO "+"`"+elt+"`"+"(Localites,Nbre_Cas) values("+"'DAKAR_"+str(j[1])+"'"+","+"'"+str(n[1])+"'"+")"
                                                curseur.execute(request2)
                                                #print(request2)
                                    else:
                                        request2 = "INSERT IGNORE INTO "+"`"+elt+"`"+"(Localites,Nbre_Cas) values("+"'DAKAR_"+str(j[1])+"'"+","+"'"+str(n[1])+"'"+")"
                                        curseur.execute(request2)
                    else:
                        if(k[1] not in ListeNO):
                            #print(k[1]) #Nom Region
                            for j in enumerate(json_obj[elt][k[1]]):
                                #print(j[1]) 
                                for o in enumerate(json_obj[elt][k[1]][j[1]]):
                                    #print(o[1]) #Nbre de cas
                                    request1 = "SELECT Localites from "+"`"+elt+"`"+" "
                                    curseur.execute(request1)
                                    Regin=curseur.fetchall()
                                    if(len(Regin)!=0):
                                        for i in Regin:
                                            if(k[1]==i[0]):
                                                #print("Dans la base")
                                                request3 = "UPDATE "+"`"+elt+"`"+" SET Nbre_Cas=Nbre_Cas+"+str(int(o[1]))+" WHERE Localites="+"'"+i[0]+"'"+""
                                                #print(request3)
                                                curseur.execute(request3)
                                            else:
                                                #print(" Pas dans la base")
                                                request2 = "INSERT IGNORE INTO "+"`"+elt+"`"+"(Localites,Nbre_Cas) values("+"'"+str(k[1])+"'"+","+"'"+str(o[1])+"'"+")"
                                                curseur.execute(request2)
                                                #print(request2)
                                    else:
                                        request2 = "INSERT IGNORE INTO "+"`"+elt+"`"+"(Localites,Nbre_Cas) values("+"'"+str(k[1])+"'"+","+"'"+str(o[1])+"'"+")"
                                        curseur.execute(request2)
                else:
                    Liste=[]
                    if (k[1]=="id_com"):
                        request = ("INSERT IGNORE INTO Communiques (id_communique) values("+json_obj[elt]["id_com"]+")")
                        curseur.execute(request)
                        id_com_temp=json_obj[elt]["id_com"]

                    if (k[1]=="date"):
                        request1 = ("UPDATE Communiques SET date="+"'"+json_obj[elt]["date"]+"'"" WHERE id_communique="+id_com_temp+"")
                        curseur.execute(request1)
                    
                    if (k[1]=="nb_test"):
                        request2 = ("UPDATE Communiques SET nb_test="+"'"+json_obj[elt]["nb_test"]+"'"" WHERE id_communique="+id_com_temp+"")
                        curseur.execute(request2)

                    if (k[1]=="nb_nv_cas"):
                        request3 = ("UPDATE Communiques SET nb_nv_cas="+"'"+json_obj[elt]["nb_nv_cas"]+"'"" WHERE id_communique="+id_com_temp+"")
                        curseur.execute(request3)

                    if (k[1]=="nb_cas_contact"):
                        request4 = ("UPDATE Communiques SET nb_cas_contact="+"'"+json_obj[elt]["nb_cas_contact"]+"'"" WHERE id_communique="+id_com_temp+"")
                        curseur.execute(request4)


                    if (k[1]=="nb_cas_communautaire"):
                        request5 = ("UPDATE Communiques SET nb_cas_communautaire="+"'"+json_obj[elt]["nb_cas_communautaire"]+"'"" WHERE id_communique="+id_com_temp+"")
                        print(json_obj[elt]["nb_cas_communautaire"])
                        curseur.execute(request5)

                    if (k[1]=="nb_gueris"):
                        request6 = ("UPDATE Communiques SET nb_gueris="+"'"+json_obj[elt]["nb_gueris"]+"'"" WHERE id_communique="+id_com_temp+"")
                        curseur.execute(request6)

                    if (k[1]=="nb_deces"):
                        request7 = ("UPDATE Communiques SET nb_deces="+"'"+json_obj[elt]["nb_deces"]+"'"" WHERE id_communique="+id_com_temp+"")
                        curseur.execute(request7)

                    if (k[1]=="date_heure_extraction"):
                        request8 = ("UPDATE Communiques SET date_extraction="+"'"+json_obj[elt]["date_heure_extraction"]+"'"" WHERE id_communique="+id_com_temp+"")
                        curseur.execute(request8)
        
        
        for i, elt in enumerate(ListeDATE):
            #print(elt)
            for k in enumerate(json_obj[elt]):
                #print(k[1])
                if(k[1] not in ListeNO):
                    if(k[1]!="DAKAR" ):
                        #print(k[1]) #Nom Region
                        for j in enumerate(json_obj[elt][k[1]]):
                            #print(j[1]) 
                            for o in enumerate(json_obj[elt][k[1]][j[1]]):
                                request = "SELECT Nbre_Cas from "+"`"+elt+"`"+" WHERE Localites="+"'"+k[1]+"'"+""
                                curseur.execute(request)
                                Nbre_Cas=curseur.fetchone()
                                request1 = "UPDATE Regions SET Nbre_Cas=Nbre_Cas+"+str(Nbre_Cas[0])+" WHERE NomRegion="+"'"+k[1]+"'"+""
                                curseur.execute(request1)
                    else:
                        pass
        my_w=Tk()
        my_w.title(lesMois[MOIS].upper())
        my_w.geometry("260x110")
        var = StringVar()
        lbl = Label(my_w, textvariable=var)
        var.set("Voulez vous valider l'importation du mois:\n"+lesMois[MOIS].upper()+"" )
        lbl.grid(row=0, column=0)
        b1=Button(my_w,text="Oui",command=lambda: com())
        b1.grid(row=1,column=0)
        b2=Button(my_w,text="Non",command=lambda: rback())
        b2.grid(row=2,column=0)
        my_w.mainloop()

     #else:
        #print("Pas de données enregistrées pour le mois: "+lesMois[j].upper()+"")                    
    ListeDATE[:] = []

curseur.close()
con.close()


