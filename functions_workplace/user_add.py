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
