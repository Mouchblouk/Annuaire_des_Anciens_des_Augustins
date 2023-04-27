#!../python.exe
import cgi
import pandas as pd
"""Ce programme recherche les données reçues par la requête dans la base de donnée, et envoie en réponse les lignes correspondantes sous forme de tableau HTML
Si aucun paramètre n'est donnée, le programme renvoie l'entièreté de la base de données"""


print("Content-Type: text/html; charset=utf-8\n")   # défini le type de la réponse à la requête
data = cgi.FieldStorage()   # récupère les données de la requête
prenom = data.getvalue('prenom')
nom = data.getvalue('nom')
annee_bac = data.getvalue('annee_bac')
email = data.getvalue('email')

database = pd.read_csv("database/anciens_eleves.csv") # ATTENTION il faut renseigner le chemin relatif de la base de donnée depuis le fichier 'serveur.py'
search_data = database

if prenom != None:
    search_data = search_data.loc[(database["prenom"]==prenom), :]
if nom != None:
    search_data = search_data.loc[(database["nom"]==nom), :]
if annee_bac != None:
    annee_bac = int(annee_bac)
    search_data = search_data.loc[(database["annee_bac"]==annee_bac), :]
if email != None:
    search_data = search_data.loc[(database["email"]==email), :]

search_data = search_data.reset_index()
search_data = search_data.loc[:, ["prenom", "nom", "annee_bac", "email"]] # enlève la ligne "index" rajouté par la fonction '.reset_index()'
if search_data.empty :  # teste si un résultat correspond à la recherche
    print("Aucun résultat ne correspond à votre recherche") # réponse à la requête si aucun résultat ne correspond

else :
    reponse =""
    for i in range(len(search_data)):   # création d'un tableau  html contenant les éléments correspondant à la recherche
        reponse += """    <tr>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
    </tr>
""".format(search_data.loc[i, "prenom"], search_data.loc[i, "nom"], search_data.loc[i, "annee_bac"], search_data.loc[i, "email"])


    print("""<table>
    <thead>
        <tr>
            <th>Prénom</th>
            <th>Nom</th>
            <th>Année du Bac</th>
            <th>Adresse e-mail</th>
        </tr>
    </thead>
""", reponse, """</table>""") # réponse à la requête
