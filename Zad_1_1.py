### Zadanie 1.1 | Interakcja i proste obliczenia (ok. 2 godz.)

# Napisz program, który prosi użytkownika (przez `input()`), żeby podał, ile kosztuje kilo ziemniaków. Niech program
# policzy i wyświetli, ile trzeba będzie zapłacić za pięć kilo ziemniaków.

# Potem napisz program, który prosi użytkownika (przez `input()`), żeby podał, ile kosztuje kilo ziemniaków i ile
# kilo chce kupić. Niech program policzy i wyświetli, ile trzeba będzie zapłacić za te ziemniaki.

# Potem napisz program, który prosi użytkownika (przez `input()`), żeby podał, ile kosztuje kilo ziemniaków,
# ile kilo ziemniaków chce kupić, ile kosztuje kilo bananów i ile kilo bananów chce kupić. Niech program policzy i
# wyświetli, ile trzeba będzie zapłacić za te ziemniaki i banany razem. I niech program sprawdzi i powie,
# za co trzeba będzie zapłacić więcej - za banany czy za ziemniaki.​

# ROZWIAZANIE
# wersja 1

cena = int(input("Ile PLN kosztuje kilogram ziemniakow?: "))
ilosc = int(input("Ile kilogramow ziemniakow chcesz kupic?: "))

zaplata = cena * ilosc

print(f"Do zaplaty jest {zaplata} PLN")

# wesrja 2

cena_ziemniaki = int(input("Ile PLN kosztuje kilogram ziemniakow?: "))
ilosc_ziemniaki = int(input("Ile kilogramow ziemniakow chcesz kupic?: "))

cena_banany = int(input("Ile PLN kosztuje kilogram bananów?: "))
ilosc_banany = int(input("Ile kilogramow bananów chcesz kupic?: "))

zaplata_ziemniaki = cena_ziemniaki * ilosc_ziemniaki
zaplata_banany = cena_banany * ilosc_banany

zaplata_razem = zaplata_banany + zaplata_ziemniaki

drozsze = "null"

if zaplata_ziemniaki > zaplata_banany:
    drozsze = "ziemniaki"
else:
    drozsze = "banany"



print(f"Razem do zaplaty jest {zaplata_razem} PLN, wiecej trzeba bedzie zaplacic za {drozsze}.")
