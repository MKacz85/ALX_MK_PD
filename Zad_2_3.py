### Zadanie 2.3
# Napisz program, który odczytuje od użytkownika wiele liczb.
# Program powinien wyliczyć i na końcu wypisać następujące statystyki:
# - liczba podanych liczb (ile sztuk), \
# - suma,
# - średnia,
# - minimum
# - maksimum
# NIE używaj funkcji wbudowanych!

# ROZWIAZANIE

liczby = None
ilosc_liczb = 0
suma = 0
srednia = None
minimum = None
maksimum = None


while True:
    liczba = (input("Wpisz liczbe lub wpisz 'KONIEC' aby zakonczyc: "))
    if liczba == "KONIEC":
        break

    if liczba.isdecimal() is False:
        print(f"Niepoprawna liczba")
        continue

    else:
        liczba = int(liczba)
        ilosc_liczb = ilosc_liczb + 1
        suma = suma + liczba
        srednia = suma / ilosc_liczb

        if maksimum is None or liczba > maksimum:
            maksimum = liczba
        if minimum is None or liczba < minimum:
            minimum = liczba
print(f"Ilosc wpisanych liczb to {ilosc_liczb}")
print(f"Suma wpisanych liczb to {suma}")
print(f"Srednia wpisanych liczb to {srednia}")
print(f"Minimalna wpisana liczba to {minimum}")
print(f"Maksymalna wpisana liczba to {maksimum}")