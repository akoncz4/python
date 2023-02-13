atlag=float(input("Add meg az évvégi átlagod "))
if atlag<=1.4:
    print("Elégtelen")
else:
    if atlag<=2.4:
        print("Elégséges")
    else:
        if atlag<=3.4:
            print("Közepes")
        else:
            if atlag<=4.4:
                print("Jó")
            else:
                if atlag>=4.5:
                    print("Jeles")
