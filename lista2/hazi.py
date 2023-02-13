print("Lista feltöltése véletlen számokkal")
import random
lista=[]
i=1
while i<=20:
    vsz=random.randint(1,20)
    lista.append(vsz)
    i=i+1
print("A lista feltöltve értékekkel")
print(lista)