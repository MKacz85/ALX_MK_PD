# ## Zadanie 1.4 | Opłata hotelowa (ok 1,5 godz.)
# Potem napisz taki program: użytkownik podaje swój wiek i ile nocy
# spędzi w hotelu, a program wylicza, ile trzeba zapłacić. Zasady są takie: nieletni (poniżej 18 roku życia) płacą
# 100 zł za noc dorośli (ci, którzy mają przynajmniej 18 lat ale mniej niż 65 lat) płacą: - 200 zł za noc,
# jeśli nocują jedną noc - 180 zł za noc, jeśli nocują przynajmniej dwie ale mniej niż pięć nocy - 150 zł za noc,
# jeśli nocują pięć lub więcej nocy - emeryci (ci, którzy mają przynajmniej 65 lat), płacą jak dorośli,
# ale z 10% zniżki Przykładowo: jeśli użytkownik ma 70 lat i spędzi w hotelu dziesięć nocy, zapłaci 150 zł za noc z
# 10% zniżki, czyli 150-15 zł za noc, czyli 135 zł za noc, czyli 1350 zł.

#ROZWIAZANIE

wiek = int(input("Podaj swoj wiek: "))
liczba_nocy = int(input("Podaj liczbe nocy spedzonych w hotelu: "))
cena = None
do_zaplaty = None
znizka_dla_emerytow = 1 - 0.1

if wiek < 18:
    cena = 100
    do_zaplaty = cena * liczba_nocy
elif 18< wiek < 65 and liczba_nocy == 1:
    cena = 200
    do_zaplaty = cena * liczba_nocy
elif 18< wiek < 65 and 1<liczba_nocy <5:
    cena = 180
    do_zaplaty = cena * liczba_nocy
elif 18< wiek < 65 and 5<liczba_nocy:
    cena = 150
    do_zaplaty = cena * liczba_nocy
elif 65 < wiek and liczba_nocy == 1:
    cena = 200 * znizka_dla_emerytow
    do_zaplaty = cena * liczba_nocy
elif 65 < wiek and 1 < liczba_nocy < 5:
    cena = 180 * znizka_dla_emerytow
    do_zaplaty = cena * liczba_nocy
elif 65 < wiek and 5 < liczba_nocy:
    cena = 150 * znizka_dla_emerytow
    do_zaplaty = cena * liczba_nocy
print(f"Zaplacisz {do_zaplaty} PLN")