from user_inscription import *

category = {"Poussin": [], "Cadet": [], "Junior": [], "Semi-pro": [], "Pro": []}

candidat_surname = (input("Veuillez renseigner le nom\n")).capitalize()
candidat_name = (input("Veuillez renseigner le prénom\n")).casefold()
candidat_birth_year = ""
candidat_email = user_email(candidat_surname, candidat_name)

# candidat_birth_year = int(user_birth_year(candidat_birth_year))

while user_birth_date_check(candidat_birth_year):
    candidat_birth_year = input("Veuillez renseigner votre date de naissance\n")

candidat_birth_year = int(candidat_birth_year)
candidat_age = user_age(candidat_birth_year)
candidat_category = user_category(candidat_age)

candidat = [candidat_surname, candidat_name, candidat_email, candidat_category]

if candidat[3] == "Non admis":
    print("Le candidat ne peut être inscrit à cause de son âge\n")
else:
    user_add(candidat, category)

# print(candidat_surname, candidat_name, candidat_email, candidat_birth_year, candidat_age)
# print(candidat)
print(category)
