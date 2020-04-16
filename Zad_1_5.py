# Zadanie 1.5 | Pole trójkąta (ok. 1 godz.) Program, który odczytuje trzy liczby, sprawdza czy liczby te mogą
# stanowić boki trójkąta (np. z 2, 2 i 5 nie da się ułożyć trójkąta, prawa?), a jeśli mogą, oblicza pole powierzchni
# trójkąta o takich bokach. Wykorzystaj trzeci wzór z [listy](https://www.matemaks.pl/wzory-na-pole-trojkata.html).
# Tutaj użyj jednego z poznanych sposobów komunikacji z użytkownikiem. Pierwiastek kwadratowy to: import math x =
# math.sqrt(10)

# ROZWIAZANIE

while True:

    import math

    a = input("Podaj liczbe a: ")
    b = input("Podaj liczbe b: ")
    c = input("Podaj liczbe c: ")

    if a.isdecimal() is False or b.isdecimal() is False or c.isdecimal() is False:
        print("Jedna lub wiecej liczb jest niepoprawnych")
        continue

    a = int(a)
    b = int(b)
    c = int(c)

    if a == max(a,b,c) and a>=b+c:
        print("Z podanych wartosci nie powstanie trojkat. Podaj inne wartosci.")
    elif b == max(a,b,c) and b>=a+c:
        print("Z podanych wartosci nie powstanie trojkat. Podaj inne wartosci.")
    elif c == max(a,b,c) and c>=a+b:
        print("Z podanych wartosci nie powstanie trojkat. Podaj inne wartosci.")
        continue

    if (a + b + c)/2>2:
        p = (a+b+c)/2
        Pole = math.sqrt(p*(p-a)*(p-b)*(p-c))
        print(f"Pole trojkata wynosi: {Pole:.2f}")


