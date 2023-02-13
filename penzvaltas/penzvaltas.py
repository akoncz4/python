def calculate_banknotes(amount):
    banknotes = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50]
    result = {}
    for banknote in banknotes:
        result[banknote] = amount // banknote
        amount = amount % banknote
    return result

amount = int(input("Adja meg az összeget: "))
banknotes = calculate_banknotes(amount)
for key, value in banknotes.items():
    if value > 0:
        print(f"{value} db {key} Ft-os bankjegy kell.")
