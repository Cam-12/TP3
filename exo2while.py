import time

nombre= int(input("Entrez un nombre : "))

if nombre>0:
    while nombre!=1:
        i= nombre-1
        time.sleep(1)
        print(i)
else:
    print("Le nombre n'est pas positif")