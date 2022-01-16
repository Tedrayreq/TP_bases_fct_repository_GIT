from datetime import datetime
import csv
from operator import truediv
import os, sys
import os.path

def user_birth_date_check(year):
    continuer = True
    if len(year) == 4:
        continuer = False
    else:
        print("Veuillez rentrez une année au format AAAA")
    return continuer


def check_length_max_input(data, length_max):
    continuer = True
    if 0 < len(data) <= length_max:
        continuer = False
    elif len(data) > length_max:
        print("L'entrée est trop longue, inscription impossible.")
        print("Veuillez contactez l'administrateur programme ou l'abréger.\n")
    return continuer


def check_user_input_num(data, com="Veuillez utilisez des chiffres"):
    continuer = True
    if data == "godmode":
        continuer = False
        return continuer
    else:
        try:
            year = int(data)
        except ValueError:
            print(com)
        else:
            continuer = False
        finally:
            return continuer


def user_email(surname, name):
    email_template = "@baton-rouge.fr"
    email = surname[0] + "." + name + email_template
    return email


def user_age(birth_year):
    return 2022 - birth_year


def user_category(age):
    if age < 6 or age > 40:
        return "Non admis"
    elif 6 < age < 12:
        return "Poussin"
    elif 12 < age < 18:
        return "Cadet"
    elif 18 < age < 24:
        return "Junior"
    elif 24 < age < 30:
        return "Semi-pro"
    elif 30 < age <= 40:
        return "Pro"
    else:
        print("Quelque chose s'est mal passé")


def user_add(user, dico):
    continuer = True
    while continuer:
        print("\nNom : ", user[0], "\nprenom : ", user[1], "\nemail : ", user[2], "\ncatégorie : ", user[3], "\n")
        correct = input("Données correcte ? y/n\n")
        if correct == "y":
            dico[user[3]].append([user])
            print("---------------------")
            print("inscription réussie")
            print("---------------------\n")
            continuer = False
        elif correct == "n":
            print("--------------------")
            print("inscription annulée")
            print("--------------------\n")
            continuer = False
        else:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("-------------------------------------------------")
            print("Veuillez rentrer 'y' ou 'n'")
            print("-------------------------------------------------\n")


def affichage_liste(dico):
    for item in dico:
        print(item, dico[item])

def name_file():
    current_date_brut = datetime.now()
    current_date = current_date_brut.strftime("%Y-%m-%d")
    file_name = "inscrits-" + current_date + ".csv"
    return file_name

# à partir de là, ça foire.
# impossible de définir un chemin relatif, ma fonction me retourne False même si le fichier existe
def check_file(name_file):
    chemin = "/csvfolder/" + str(name_file)
    is_file = os.path.exists(chemin)
    return is_file


def save_file(dico):
    with open('csvfolder\\' + file_name, 'a') as csv_file:
        monwriter = csv.writer(csv_file, delimiter=';')
        dirs = os.listdir('csvfolder\\')
        entete = "nom;prénom;mail;catégorie"
        for file in dirs:
            print(file)
        if entete in dirs:
            for i in dico:
                monwriter.writerow([i])
                for j in dico[i]:
                    monwriter.writerow([j[0], j[1], j[2], j[3]])
        else :
            monwriter.writerow(entete)
            for i in dico:
                monwriter.writerow([i])
                for j in dico[i]:
                    monwriter.writerow([j[0], j[1], j[2], j[3]])

# with open('test.csv', 'w') as csv_file:
#     monwriter = csv.writer(csv_file, delimiter=';')
#     monwriter.writerow(["toto"]+["tata"])
#     monwriter.writerow(["titi", "tutu"])

# {"Poussin": [[nom, prenom, mail, cat], [nom, prénom, mail, cat]], "Cadet": [], "Junior": [], "Semi-pro": [], "Pro": []}