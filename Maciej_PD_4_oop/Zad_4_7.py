# Do zadania z klasą `Ogloszenie` dodaj kolejne kolejne klasy, które po niej dziedziczą.
# `OgloszenieSamochodowe` – dziedziczy z `Ogloszenie` i dodatkowo określa cechy sprzedawanego samochodu jak model, markę, rok produkcji, przebieg, pojemność, moc i rodzaj paliwa.
# `OgloszenieMieszkaniowe` – też dziedziczy z `Ogloszenie`, a dodatkowo cechy sprzedawanego mieszkania / domu: miejscowość, metraż, liczba pokoi.

from Maciej_PD_4_oop.Zad_4_1 import Ogloszenie

class OgloszenieSmochodowe(Ogloszenie):
    def __init__(self, tytul, opis, dane_kontaktowe, numer: int, marka: str, model: str, cena: int, rocznik: int, przebieg: int, paliwo: str):
        super().__init__(tytul, opis, cena, dane_kontaktowe)
        self.numer = numer
        self.marka = marka
        self.model = model
        self.rocznik = rocznik
        self.przebieg = przebieg
        self.paliwo = paliwo
        self.moc = 0
        self.pojemnosc = 0


class OgloszenieMieszkaniowe(Ogloszenie):
    def __init__(self, tytul, opis, cena, dane_kontaktowe, miejscowosc: str, metraz: int, liczba_pokoi: int):
        super().__init__(tytul, opis, cena, dane_kontaktowe)
        self.miejscowosc = miejscowosc
        self.metraz = metraz
        self.liczba_pokoi = liczba_pokoi
