import random #as veletlen
vsz=random.randint(1,10)
print("Az előállított véletlen számom: ", vsz)
i = 0
while i < 10:
    vsz=random.randint(1,10)
    if (vsz%2==0):
        print("Az előállított véletlen számom: ", vsz)
        i=i+1
print("Vége") 
j=0
print("3-al és 5-el osztható számokat írja ki")
while (j<10):
    vsz1=random.randint(1,100)
    if (vsz1%3==0 and vsz1%5==0):
        print("A szám: ", vsz1)
        j=j+1
print("Ennek is vége")