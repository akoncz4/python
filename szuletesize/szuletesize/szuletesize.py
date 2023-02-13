
szev=int(input("Add meg a születési évedet "))
szho=int(input("Add meg a születési hónapodat (pl. 10) "))
sznap=int(input("Add meg a születési napodat "))
kornap=int((szev*365)+(szho*30)+sznap)
maev=int(input("Add meg a mai évet "))
maho=int(input("Add meg a mai hónapot "))
manap=int(input("Add meg a mai napot "))
manapok=int((maev*365)+(maho*30)+manap)
kor=manapok-kornap
ev=int(kor/365)
kor=(kor-(ev*365))
ho=int(kor/30)
kor=(kor-(ho*30))
print(ev, "éves ", ho, "hónapos ", kor, "napos")
if ev>=18:
    print("nagykorú")
else:
        print("kiskorú")