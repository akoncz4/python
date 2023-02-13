print("Összegzés, átlag, max és min")
import random
i=0
ossz=0
max=0
min=11
sormax=0
sormin=0
while i<10:
    vsz=random.randint(1,10)
    print("Az ", i, ". szám->", vsz)
    ossz=ossz+vsz
    if(max<vsz):
        max=vsz
        sormax=i
    if(min>vsz):
        min=vsz
        sormin=i

    i=i+1
print("A legkisebb szám: ", min, "sorszáma: ", sormin)
print("A legnagyobb szám: ", max, "sorszáma: ", sormax)
print("A számok összege: ", ossz)
print("A számok átlaga: ", (ossz/i))
print("A program vége")