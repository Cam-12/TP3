nombre=int(input("Entrez un nombre : "))
a= 0

for i in range(0, nombre, 1):
    a= a+i
    if a>=nombre:
        print(i)
        break