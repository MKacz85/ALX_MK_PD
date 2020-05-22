# Stwórz klasę `Pociag`. Klasa niech ma dwa atrybuty: predkość (początkowa wartość to 10) i ilosc_paliwa (początkowa wartość to 1000).
# Dodaj do klasy `Pociag` metode `opis`. Ta metoda niech zwraca napis o treści "Moja predkość to (ileś tam). Mam jeszcze (ileś tam) litrów paliwa."
# Dodatkowo zaimplementuj metodę `__str__`.
# Dodaj metode `przyspiesz`. Ta metoda niech przyjmuje jeden argument mówiący, o ile ma zwiekszyć się prędkość.
# Ta metoda niech zwiększa predkość pociągu o tyle, ile jest powiedziane w argumencie.
# I niech zmniejsza ilość paliwa o: `(nowa predkosc - stara_predkosc) * (stara predkosc / 100)`.
# Niech nie da się jednorazowo zwiększyć prędkości o więcej niż 75% (jeśli ktoś spróbuje tak zwiększyć prędkość,
# prędkość niech pozostaje po prostu bez zmian). Niech nie da sie zwiększyć prędkości,
# jeśli pociąg nie ma juz paliwa (jeśli ktoś spróbuje zwiększyć prędkość, kiedy nie ma paliwa, prędkość niech pozostaje po prostu bez zmian).
# Przetestuj swoje rozwiązanie i napisz testy, w których:
#
# - zwiększysz prędkość pociągu o 5 km/h i wypisze jego opis
#
# - zwiększysz prędkość pociągu o 20 km/h i wypisze jego opis
#
# - zwiększysz prędkość pociągu o 8 km/h i wypisze jego opis
#
# - zwiększysz prędkość pociągu o 10 km/h i wypisze jego opis

# ROZWIĄZANIE
# Stwórz klasę `Pociag`. Klasa niech ma dwa atrybuty: predkość (początkowa wartość to 10) i ilosc_paliwa (początkowa wartość to 1000).

class Pociag:
    def __init__(self, predkosc: int, ilosc_paliwa: int):
        self.predkosc = predkosc
        self.ilosc_paliwa = ilosc_paliwa

    # Dodaj do klasy `Pociag` metode `opis`. Ta metoda niech zwraca napis o treści "Moja predkość to (ileś tam). Mam jeszcze (ileś tam) litrów paliwa."
    def get_info(self) -> str:
        return f'Moja prędkość to {self.predkosc} km/h, mam jeszcze {self.ilosc_paliwa} litrów paliwa'

    # Dodatkowo zaimplementuj metodę `__str__`.
    def __str__(self) -> str:
        return self.get_info()

    # Dodaj metode `przyspiesz`. Ta metoda niech przyjmuje jeden argument mówiący, o ile ma zwiekszyć się prędkość.
    def przyspiesz(self, przyspieszenie: int):
        if self.ilosc_paliwa <= 0:
            raise TypeError("Nie ma już paliwa")
        else:
            if przyspieszenie <= self.predkosc * 0.75 and self.ilosc_paliwa > (self.predkosc+przyspieszenie - self.predkosc) * self.predkosc / 100:
                stara_predkosc = self.predkosc
                self.predkosc = self.predkosc + przyspieszenie
                self.ilosc_paliwa -= (self.predkosc - stara_predkosc) * stara_predkosc / 100
            else:
                print("Nie możesz tyle przyśpieszyć, brakuje paliwa!")
        return self.predkosc



tgv = Pociag(100, 100)
tgv.przyspiesz(80)
tgv.przyspiesz(0)
info = tgv.get_info()
print(info)

# TESTY

def test_zwieksz_predkosc_o_5():
    tgv = Pociag(100,100)
    assert tgv.przyspiesz(5) == 105

def test_zwieksz_predkosc_o_20():
    tgv = Pociag(100,100)
    assert tgv.przyspiesz(20) == 120

def test_zwieksz_predkosc_o_8():
    tgv = Pociag(100,100)
    assert tgv.przyspiesz(8) == 108

def test_zwieksz_predkosc_o_10():
    tgv = Pociag(100,100)
    assert tgv.przyspiesz(10) == 110