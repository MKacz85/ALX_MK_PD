# Stwórz klasę `Zbiornik`. Niech ta klasa ma tylko jeden atrybut: `ilosc_wody` (z początkową wartością 0).
# Niech ta klasa ma metody `dolej` i `odlej`. Obie metody niech przyjmują argument `ile` i niech odpowiednio dodają lub odejmują tę liczbę do atrybutu `ilosc_wody`.
# Niech nie da się odlać więcej wody, niż jest w zbiorniku.
# Niech obiekt klasy `Zbiornik` po skonwertowaniu na napis dawał napis `zbiornik z (ileś tam) litrami wody`.
# Przerób klasę `Zbiornik` tak, żeby miała też drugi atrybut - `temperatura`.
# Metoda dolej oprócz argumentu `ile` powinna też przyjmować argument `temperatura` oznaczający temperaturę dolewanej wody.
# Dolanie wody do zbiornika powinno powodować zmianę temperatury wody w zbiorniku (zgodnie ze zwykłymi prawami fizyki).

# ROZWIAZANIE
# Stwórz klasę `Zbiornik`. Niech ta klasa ma tylko jeden atrybut: `ilosc_wody` (z początkową wartością 0).

class Zbiornik:
    def __init__(self, ilosc_wody: int):
        self.ilosc_wody = 0

    # Niech ta klasa ma metody `dolej` i `odlej`. Obie metody niech przyjmują argument `ile` i niech odpowiednio dodają lub odejmują tę liczbę do atrybutu `ilosc_wody`.

    def dolej(self, ile: int):
        self.ilosc_wody += ile
        return self.ilosc_wody

    # Niech nie da się odlać więcej wody, niż jest w zbiorniku.
    def odlej(self, ile: int):
        if self.ilosc_wody > ile:
            self.ilosc_wody -= ile
        else:
            print(f'Nie da sie odlać tyle wody')
        return self.ilosc_wody

    # Niech obiekt klasy `Zbiornik` po skonwertowaniu na napis dawał napis `zbiornik z (ileś tam) litrami wody`.
    def get_info(self) -> str:
        return f'Zbiornik z {self.ilosc_wody} litrami wody'

    def __str__(self) -> str:
        return self.get_info()


# Przerób klasę `Zbiornik` tak, żeby miała też drugi atrybut - `temperatura`.


class ZbiornikTemp:
    def __init__(self, ilosc_wody: int, temp: int):
        self.ilosc_wody = 0
        self.temp = 0

    # Metoda dolej oprócz argumentu `ile` powinna też przyjmować argument `temperatura` oznaczający temperaturę dolewanej wody.

    def dolej_z_temp(self, ile: int, temp: int):
        self.temp = (self.ilosc_wody * self.temp + ile * temp) / (self.ilosc_wody + ile)
        self.ilosc_wody += ile

        return self.temp and self.ilosc_wody


    def odlej_z_temp(self, ile_wody:int, temp: int):
        if self.ilosc_wody > ile_wody:
            self.ilosc_wody -= ile_wody
        else:
            print(f'Nie da sie odlać tyle wody')
        return self.ilosc_wody

    def get_info(self) -> str:
        return f'Zbiornik z {self.ilosc_wody} litrami wody o temperaturze {self.temp:.2f} C'

    def __str__(self) -> str:
        return self.get_info()


Kubek = ZbiornikTemp(0,0)
Kubek.dolej_z_temp(20,60)
Kubek.dolej_z_temp(20,60)
info = Kubek.get_info()
print(info)