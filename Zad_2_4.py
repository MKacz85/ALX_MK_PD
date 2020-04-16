# Zadanie 2.4 | Zgadnij liczbę z zakresu

# Program losuje liczbę z zakresu od 0 do 999. Użytkownik ma zgadnąć tę liczbę nie widząc jej. Kiedy użytkownik poda
# nieprawidłowy wynik, program podpowiada pisząc czy podana liczba była za duża, czy za mała. Gdy użytkownik poda
# właściwą liczbę, program wypisuje gratulacje jednocześnie informując, w której próbie udało się zgadnąć liczbę.

# Nawiasem mówiąc technika wyszukiwania oparta o "podpowiedzi" za dużo/za mało nazywa się bisekcją i pełni w
# informatyce bardzo ważną rolę. Umiejętnie ją stosując powinno się te zagadki rozwiązywać w 9-10 próbach (bo
# 2^10=1024).

# ROZWIAZANIE

from random import randint

x = randint(0, 999)
proby = 0
while True:
    y = input("Podaj liczbe: ")

    if y.isdecimal() is False:
        print(f"Niepoprawna liczba")
        continue
    else:
        y = int(y)
        proby = proby + 1
        if x == y:
            print(f"BRAWO, podales poprawna liczbe po {proby} probach!")
            break
        elif x>y:
            print(f"Podana liczba jest za mala")
        elif x<y:
            print(f"Podana liczba jest za duza")