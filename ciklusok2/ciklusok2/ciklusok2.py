#1
print("10-től 20-ig számolás")
i=10
while i<=20:
    print(i)
    i=i+1
print("10-20-ig összeadás")
#2
u=10
szamol=0

while u<=20:
    szamol += u
    u += 1
print(szamol)
#3
print("10-20-ig a számok átlaga")
lista=[10,11,12,13,14,15,16,17,18,19,20]
atlag=sum(lista)/len(lista)
print("A számok átlaga", atlag)
#4
a=int(input("Adj meg egy változót"))
b=int(input("Adj meg egy másik változót"))
#5