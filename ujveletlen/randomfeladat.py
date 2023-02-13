import random
j=0
while (j<20):
    vsz=random.randint(1,20)
    print("A szám: ", vsz)
    if (vsz%3==0):
        j=j+1
print("Ennyi darab szám van:", vsz)
print("vége")