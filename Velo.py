heureDepart= int(input("Donnez l’heure de début de la location (un entier) : "))
heureFin= int(input("Donnez l’heure de fin de la location (un entier) : "))
prix=0

while heureDepart>0 or heureDepart<24:
    print("Les heures doivent être comprises entre 0 et 24 !")
while heureFin>0 and heureFin<24:
    print("Les heures doivent être comprises entre 0 et 24 !")

if heureDepart<heureFin:
    if heureDepart<7 and heureDepart>0:
        temps= heureFin-heureDepart
        prix= temps * 1
