import random

x= random.randint(0, 100)
nombre= int(input("Entrez un nombre : "))
i=0

while x!=nombre:
    if nombre<x:
        nombre= int(input("Nombre plus grand ! Entrez un nombre : "))
    elif nombre>x:
        nombre= int(input("Nombre plus bas ! Entrez un nombre : "))
    i= i+1

print("Nombre trouver en", i, "essai")