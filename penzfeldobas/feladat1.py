import random
dobasok=int(input("Add meg a dobások számát: "))
fej = 0
írás = 0
fejviras=str(input("Add meg, hogy a fejeket vagy az írásokat számolja (fej , iras): "))
if fejviras == 'fej':
    while dobasok >= 1:
        erme = random.randint(0,1)
        if erme == 0:
            print("fej")
        fej = fej+1
        print("A fejek száma: ", fej)
    else:
        if fejviras == 'iras':
            while dobasok >= 1:
                erme=random.randint(0,1)
            print("írás")
    írás = írás+1
    dobasok=dobasok-1
print("Az írások száma: ", írás)

print("Fejek száma: ", fej)
print("Írások száma: ", írás)

if fej>írás:
    print("Több fej van")
else:
    print("Több írás van")
