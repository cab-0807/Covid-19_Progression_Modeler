
def search_(entree):
    liste_=["DakarCentre","Mboro","Point-E","CiteApecsy","Sedhiou","CiteDjilyMbaye","GrandDakar","Ngor","CiteSococim","Dieuppeul","DakarOuest","Almadies","DakarPlateau","Wakhinane","CiteFadia","Bambilor","CiteBaobab","Castors","SicapMbao","Derkle","Colobane","Gibraltar","CiteKeurGorgui","CiteTako","Arafat","CiteGadaye","DakarSud","DakarNord","Thies","Kaolack","Guediawaye","HLM","NordFoire","FassMbao","NiaryTaly","CiteSoprim","HLMFass","ZoneDeCaptage","HLMGrandMedine","Mamelles","HLMGrandYoff","Yoff","Ngaparou","Niakou-Rap","Somone","Sacre-Coeur3","Mboro","Sacre-Coeur-3","Sacre-Coeur1","Sacre-Coeur2","Mermoz","KeurMbayeFall","Sebikotane","Touba","Rufisque","Mbour","Mbao","Saint-Louis","Tivaouane","GueuleTapee","Maristes","KeurMassar","Popenguine","Pikine","Ziguinchor","Camberene","Tassette","KeurNdiayeLo","CiteMixta","Malika","BeneBarack","ZakMbao","LacRose","Yarakh","ThiaroyeSurMer","Diamniadio","OuestFoire","Louga","Kedougou","Liberte2","Liberte1","Liberte4","Richard-Toll","Kolda","SicapBaobabs","Sangalkam","Matam","FannResidence","Sokone","Liberte6","Diourbel","Fatick","Yeumbeul","Tambacounda","Velingara","Khombole","Rebeuss","Poute","Dahra","Sedhiou","Bignona","Saraya","Linguere","Kebemer","Mekhe","Kaffrine","NioroduRip","Guinguineo","ThienabaSeck","Joal","Thiadiaye","Mbacke","Podor","Goudiry","Dioffior","Coki","DarouMousty","Sakal","Bambey","Ndoffane","Passy","Saly","Dagana","Kanel","Foundiougne","Salemata","Bounkiling","Pete","Oussouye","Birkilane","Bakel","Thilogne","Koumpentoum","Koungheul","Makacoulibantang","KeurMomarSarr","Thionck-Essyl","Diouloulou","Niakhar","Liberte3","Ouakam","Medina","MedinaYoroFoula","Ranerou","Gossas","MalemHoddar","Diakhao","Kidira","DiankeMakha","Ndiassane","Goudomp","TaibaNdiaye"]
    sortie=""
    count=0
    temp=[]

    for i in range(len(liste_)):
        liste_[i]=liste_[i].lower()
        for i in range(len(liste_)):
            if(entree==""):
                sortie=entree
            if(isinstance(entree,int)):
                sortie=entree
            else:
                if(entree in liste_[i]):
                    sortie=liste_[i]
    return sortie




