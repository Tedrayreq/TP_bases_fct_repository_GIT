from datetime import datetime
import csv


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


def save_file(dico):
    current_date_brut = datetime.now()
    current_date = current_date_brut.strftime("%Y-%m-%d")
    file_name = "inscrits-" + current_date + ".csv"
    