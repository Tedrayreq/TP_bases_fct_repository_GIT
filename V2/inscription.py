from user_inscription import *

category = {"Poussin": [], "Cadet": [], "Junior": [], "Semi-pro": [], "Pro": []}

# Ajouter For ou while pour nombre d'inscrits à ajouter
compteur_inscription = 0

nombre_inscription = ""
while check_user_input_num(nombre_inscription):
    nombre_inscription = input("Combien d'inscription comptez-vous faire ?\n")
nombre_inscription = int(nombre_inscription)

while compteur_inscription != nombre_inscription:
    candidat_surname = ""
    while check_length_max_input(candidat_surname, 15):
        candidat_surname = (input("Veuillez renseigner le nom\n")).capitalize()

    candidat_name = ""
    while check_length_max_input(candidat_name, 15):
        candidat_name = (input("Veuillez renseigner le prénom\n")).casefold()

    candidat_birth_year = ""
    candidat_email = user_email(candidat_surname, candidat_name)

    com_input_birth_date = "Veuillez rentrer une année au format AAAA avec des chiffres"
    while user_birth_date_check(candidat_birth_year) or check_user_input_num(candidat_birth_year, com_input_birth_date):
        candidat_birth_year = input("Veuillez renseigner la date de naissance\n")

    candidat_birth_year = int(candidat_birth_year)
    candidat_age = user_age(candidat_birth_year)
    candidat_category = user_category(candidat_age)

    candidat = [candidat_surname, candidat_name, candidat_email, candidat_category]

    if candidat[3] == "Non admis":
        print("Le candidat ne peut être inscrit à cause de son âge\n")
    else:
        user_add(candidat, category)
    compteur_inscription += 1
# Prévoir fct pour check catégorie pour annulation inscription si déjà inscrits

# print(candidat_surname, candidat_name, candidat_email, candidat_birth_year, candidat_age)
# print(candidat)
affichage_liste(category)
