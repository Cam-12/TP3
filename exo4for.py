nombre= int(input("Entrez un nombre : "))
a=1

for i in range(1, nombre+1, 1):
    a= a*i
print("La factorielle de", nombre, "est", a)