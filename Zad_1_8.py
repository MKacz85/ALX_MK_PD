# Zadanie 1.8 | Kalkulator lat psich (ok. 0,5 godz.)
# Zakładamy, że 1 ludzki rok, to 5 lat psich.
# Za pomocą konsoli wczytaj imię i wiek psa.
# Wypisz komunikat ile pies miałby lat gdyby był człowiekiem.
# Przykład:
# Podaj imię psa - Burek
# Podaj wiek psa - 3
# Gdyby Burek był człowiekiem, miałby 15 lat.

# ROZWIAZANIE

imie_psa = input("Wpisz imie psa: ")
wiek_psa = int(input("Wpisz wiek psa: "))

print(f"Imie psa - {imie_psa}\nWiek psa - {wiek_psa}lat\nGdyby {imie_psa} byl człowiekiem miałby {wiek_psa*5} lat.")