y= 0
z= 0
a= 0

for i in range(0, 10, 1):
    x = int(input("Entrez les valeurs entre 0 et 20 : "))
    while x<0 or x>20:
        x = int(input("Entrez les valeurs entre 0 et 20 : "))
    if x<10:
        y=y+1
    elif x>=10 and x<15:
        z=z+1
    elif x>=15:
        a=a+1

print("Nombre de valeurs strictement inférieur à 10 : ", y)
print("Nombre de valeurs supérieur ou égale à 10 et strictement inférieur à 15 : ", z)
print("Nombre de valeurs supérieur ou égale à 15 : ", a)