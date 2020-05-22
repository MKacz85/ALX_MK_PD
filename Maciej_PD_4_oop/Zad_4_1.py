# Zaproponuj klasę, w której obiektach będzie się zapisywać ogłoszenia (takie jak w serwisie internetowym z ogłoszeniami).
# Najlepiej, aby klasa `Ogloszenie` opisywała rzeczy, które posiada każde ogłoszenie, m.in. tytuł, opis, cenę, dane kontaktowe sprzedawcy.

class Ogloszenie:
    def __init__(self, tytul: str, opis: str, cena: float, dane_kontaktowe: str):
        self.tytul = tytul
        self.opis = opis
        self.cena = cena
        self.dane_kontaktowe = dane_kontaktowe

    def get_info(self) -> str:
        return f'{self.tytul}' \
               f'{self.opis}' \
               f'Cena: {self.cena}' \
               f'Dane kontaktowe sprzedawcy:' \
               f'{self.dane_kontaktowe}'

    def __str__(self):
        return self.get_info


