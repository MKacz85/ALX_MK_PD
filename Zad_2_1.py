# adanie 2.1 | Zagadka matematyczna Program losuje dwie liczby z zakresu od 0 do 99 (patrz poniżej). Podaje te
# dwie liczby i pyta jaka jest ich suma (nie podaje jej). Użytkownik ma odgadnąć (no, policzyć w głowie) wynik.
# Program pyta o wynik wielokrotnie, tak długo, aż użytkownik poda prawidłowy wynik.

#ROZWIAZANIE

from random import randint

x = randint(0, 99)
y = randint(0, 99)

print(x)
print(y)

while True:

    sum = input("Jaka jest ich suma?: ")

    if sum.isdecimal() is False:
        print("Podales zla liczbe")
        continue

    sum = int(sum)
    if sum != x + y:
        print(f"{sum} nie jest poprawna suma! Sprobuj ponownie!")
        continue

    elif sum == x + y:
        print(f"{sum} jest poprawna suma!")
        break

