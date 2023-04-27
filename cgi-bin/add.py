#!../python.exe
import cgi
import pandas as pd
"""Ce programme ajoute une ligne à la base de donnée csv avec les données qui lui sont envoyés par la requête"""


print("Content-Type: text/html; charset=utf-8\n")   # défini le type de la réponse à la requête
data = cgi.FieldStorage()   # récupère les données de la requête
prenom = data.getvalue('prenom')
nom = data.getvalue('nom')
annee_bac = data.getvalue('annee_bac')
email = data.getvalue('email')

database = pd.read_csv("database/anciens_eleves.csv") # ATTENTION il faut renseigner le chemin relatif de la base de donnée depuis le fichier 'serveur.py'

if database.loc[(database["prenom"]==prenom) & (database["nom"]==nom) & (database["annee_bac"]==int(annee_bac)) & (database["email"]==email), :].empty : # vérifie si les informations données existent déjà dans la base de données
    add_data = pd.DataFrame({'prenom':[prenom], 'nom':[nom], 'annee_bac':[annee_bac], 'email':[email]})
    database = database.append(add_data)
    database.to_csv("database/anciens_eleves.csv", index=False)   # ATTENTION il faut renseigner le chemin relatif de la base de donnée depuis le fichier 'serveur.py'

    print("Contenu ajouté !") # réponse à la requête

else :
    print("Action impossible, les informations données sont déjà utilisées") # réponse à la requête
