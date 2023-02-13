a = int(input("Adj meg egy számot: "))
b = int(input("Adj meg egy másik számot: "))
c = int(input("Növekvő(1) vagy csökkenő(2) legyen a sorrend?: "))
if c==1:
    if a<b:
        while a<b:
            print(a)
            a=a+1
    else:
        while a>b:
            print(b)
            b=b+1
else:
    if c==2:
        if a<b:
            while b>a:
                print(b)
                b=b-1
        else:
            while a>b:
                print(a)
                a=a-1