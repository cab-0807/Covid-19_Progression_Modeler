import json
import pymysql
json_data= open("nom_du_fichier.json").read   
json_obj=json.loads(json_data)
con=pymysql.connect(host="localhost",user="root",password="",db="json")

cursor=con.cursor()
for item in json_obj:
    NomDate=item.get(NomDate)
    NbTest=item.get(NbTest)
    NbNouveauCas=item.get(NbNouveauCas)
    NbCasContacts=item.get(NbCasContacts)
    NbCasCommunautaire=item.get(NbCasCommunautaire)
    NbGueris=item.get(NbGueris)
    NbDeces=item.get(NbDeces)
    NomFichierSource=item.get(NomFichierSource)
    DateHeureExtraction=item.get(DateHeureExtraction)
    cursor.execute("insert into jour(NomDate,NbTest,NbNouveauCas,NbCasContacts,NbCasCommunautaire,NbGueris,NbDeces,NomFichierSource,DateHeureExtraction)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(NomDate,NbTest,NbNouveauCas,NbCasContacts,NbCasCommunautaire,NbGueris,NbDeces,NomFichierSource,DateHeureExtraction))
con.commit()
con.close()