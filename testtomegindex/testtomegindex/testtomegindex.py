testsuly=float(input("Add meg a testsúlyodat (pl. 80) "))
magassag=float(input("Add meg a magasságod (pl. 1.85) "))
bmi=testsuly/(magassag*magassag)
print("A testtömeg indexed:", bmi)
if bmi<=16:
    print("Kóros soványság")
else:
    if bmi<=17:
        print("Mérsékelt soványság")
    else:
        if bmi<=18.5:
            print("Enyhe soványság")
        else:
            if bmi<=25:
                print("Normális testsúly")
            else:
                if bmi<=30:
                    print("Túlsúly")
                else:
                    if bmi<=35:
                        print("Elhízás")
                    else:
                        if bmi<=40:
                            print("Túlzott elhízás")
                        else:
                            if bmi>40:
                                print("Extrém elhízás")
