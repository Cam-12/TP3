nombre= int(input("Entrez un nombre : "))
a=1
b=1

while a!=nombre:
    a= a+1
    b= b*a
print("La factorielle de", nombre, "est", b)