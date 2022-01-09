def user_birth_year(year):
    continuer = True
    while continuer:
        year = input("Veuillez renseigner l'année de naissance\n")
        if len(year) == 4:
            year = int(year)
            continuer = False
        else:
            print("Veuillez rentrez une année au format AAAA")
    return year
