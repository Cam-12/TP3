import time

nombre= int(input("Entrez un nombre : "))

if nombre>0:
    while nombre!=-1:
        print(nombre)
        nombre= nombre-1
        time.sleep(1)
else:
    print("Le nombre n'est pas positif")