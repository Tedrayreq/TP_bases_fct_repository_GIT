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
