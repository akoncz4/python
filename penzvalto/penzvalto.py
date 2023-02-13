ossz=int(input("Add meg a pénz összegét: "))

husze=ossz//20000
ossz=ossz%20000
tize=ossz//10000
ossz=ossz%10000
ote=ossz//5000
ossz=ossz%5000
kete=ossz//2000
ossz=ossz%2000
ezer=ossz//1000
ossz=ossz%1000
otsz=ossz//500
ossz=ossz%500
ketsz=ossz//200
ossz=ossz%200
szaz=ossz//100
ossz=ossz%100
otven=ossz//50
ossz=ossz%50
husz=ossz//20
ossz=ossz%20
tiz=ossz//10
ossz=ossz%10
ot=ossz//5
ossz=ossz%5

print(husze,"db 20 ezres kell")
print(tize,"db 10 ezres kell")
print(ote,"db 5 ezres kell")
print(kete,"db 2 ezres kell")
print(ezer,"db ezres kell")
print(otsz,"db 500-as kell")
print(ketsz,"db 200-as kell")
print(szaz,"db 100-as kell")
print(otven,"db 50-es kell")
print(husz,"db 20-as kell")
print(tiz,"db 10-es kell")
print(ot,"db 5 forintos kell")