def user_birth_date_check(year):
    continuer = True
    if len(year) == 4:
        continuer = False
    else:
        print("Veuillez rentrez une année au format AAAA")
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
        print("Quelque chose c'est mal passé")


def user_add(user, dico):
    continuer = True
    while continuer:
        print("\nNom : ", user[0], "\nprenom : ", user[1], "\nemail : ", user[2], "\ncatégorie : ", user[3], "\n")
        correct = input("Données correcte ? y/n\n")
        if correct == "y":
            dico[user[3]] = [user]
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
