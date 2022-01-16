import csv

with open('test.csv', 'w') as csvfile:
    monwriter = csv.writer(csvfile, delimiter=';')
    monwriter.writerow(["toto"]+["tata"])
    monwriter.writerow(["titi", "tutu"])