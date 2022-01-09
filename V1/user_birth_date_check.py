def user_birth_date_check(year):
    continuer = True
    if len(year) == 4:
        continuer = False
    else:
        print("Veuillez rentrez une année au format AAAA")
    return continuer
