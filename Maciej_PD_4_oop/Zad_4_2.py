# Napisz programy, w których tworzysz listę ogłoszeń samochodowych, a następnie wyszukujesz ogłoszenia na podstawie ich parametrów.
# Na przykład ogłoszenia o cenach z określonego przedziału.
# Użyj funkcji `lambda`, określających, które ogłoszenia powinny zostać wyszukane. Użyj poznanych kolekcji do trzymania ogłoszeń.
# Możesz zastosować metodę `filter` do wyszukiwania odpowiednich ogłoszeń.

# ROZWIĄZANIE

# Tworzenie ogłoszenia

class Ogloszenie:
    def __init__(self,numer: int, marka: str, model: str, cena: int, rocznik: int, przebieg: int, paliwo: str):
        self.numer = numer
        self.marka = marka
        self.model = model
        self.cena = cena
        self.rocznik = rocznik
        self.przebieg = przebieg
        self.paliwo = paliwo

    def get_info(self) -> str:
        return f'Ogloszenie numer:{self.numer}, samochód marki: {self.marka}, model: {self.model}, ' \
               f'cena: {self.cena}, rocznik: {self.rocznik}, przebieg: {self.przebieg}, paliwo: {self.paliwo}'


# Tworzenie listy przechowującej ogłoszenia

class ListaOgloszen:
    def __init__(self):
        self.items = dict()

    def add_ogloszenie(self, ogloszenie: Ogloszenie, liczba: int):

        if not isinstance(ogloszenie, Ogloszenie):
            raise TypeError

        if liczba <= 0:
            raise ValueError

        if ogloszenie in self.items:
            self.items[ogloszenie] += liczba
        else:
            self.items[ogloszenie] = liczba

    def jest_puste(self) -> bool:
        if len(self.items) > 0:
            return False
        else:
            return True

# Wyszukiwanie ogloszen

    def wyszukiwanie_marki(self):
        for marka in self.items:
            return {i: self.items(i) for i in self.marka}
