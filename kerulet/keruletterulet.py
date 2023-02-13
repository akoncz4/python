valasztas=int(input("Válaszd ki, hogy minek a területét számolja ki a program: 1->Négyzet 2->Téglalap 3->Háromszög 4->Kör"))
if valasztas >0 and valasztas <5:
    print("A megadott szám jó")
    if valasztas == 1:
        noldal=float(input("Add meg a négyzet oldalát"))
        nk=4*(noldal)
        nt=noldal*noldal
        print("A négyzet kerülete: ", round(nk,2))
        print("A négyzet területe: ", round(nt,2))
    if valasztas == 2:
        ta=float(input("Add meg a téglalap A oldalát "))
        tb=float(input("Add meg a téglalap B oldalát "))
        tk=2*(ta+tb)
        tt=ta*tb
        print("A téglalap kerülete: ",round(tk,2))
        print("A téglalap területe: ",round(tt,2))
    if valasztas == 3:
        ha=float(input("Add meg a háromszög A oldalát "))
        hb=float(input("Add meg a háromszög B oldalát "))
        hc=float(input("Add meg a háromszög C oldalát "))
        ma=float(input("Add meg a háromszög magasságát "))
        hk=ha+hb+hc
        ht=(ha*ma)/2
        print("A háromszög kerülete: ",round(hk,2))
        print("A háromszög területe: ",round(ht,2))
    if valasztas == 4:
        import math
        kr=float(input("Add meg a kör sugarát "))
        kk=2*kr*math.pi
        kt=kr*kr*math.pi
        print("A kör kerülete: ",round(kk,2))
        print("A kör területe: ",round(kt,2))

else:
    print("Nem jó adatok")
print("A program vége")