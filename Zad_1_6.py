### Zadanie 1.6 | Bilety (ok. 1 godz.)
# Założenia:

#	- 0-6   - wiek przedszkolny - cena biletu: 0

#	- 7-17  - wiek szkolny      - cena biletu: 2.28

#	- 18-64 - wiek dorosły      - cena biletu: 3.80

#	- +65   - wiek emerytalny   - cena biletu: 1.90
# Napisz program, który przyjmuje dwie informacje: jaki jest wiek osoby kupującej bilety i ile biletów chce kupić.
# Na tej podstawie i powyższych założeń policz ile zapłaci za bilety, które chce kupić. Wczytywanie danych i ich wyświetlenie zrealizuj za pomocą konsoli

# ROZWIAZANIE

wiek = int(input("Podaj swoj wiek: "))
ilosc_biletow = int(input("Podaj ilosc biletow: "))
cena_biletu = None
if 0<wiek<=6:
     cena_biletu = 0
elif 7<wiek<18:
     cena_biletu = 2.28
elif 18<= wiek<=64:
     cena_biletu = 3.8
elif 64<wiek:
     cena_biletu = 1.9

print(f"Do zaplaty za bilety jest: {cena_biletu*ilosc_biletow} PLN")
