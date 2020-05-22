# Napisz klasę `Zolw` z metodami `idz` i `obroc_sie`. Żółw ma jakieś położenie (wyrażone dwiema współrzędnymi) i jakieś ustawienie, czyli kurs (wyznaczony pojedyncza liczba).
#
# Początkowe położenie podajemy konstruktorowi klasy, początkowy kurs to zawsze 0.

# Metoda `obroc_sie ` powoduje obrót żółwia, czyli zmianę jego kursu.

# Metoda `idz` powoduje przejście żółwia o określoną odległość.

# Z klasy będzie się korzystać tak:
# ```python
# z = Zolw(100, 100)
# z.idz(50)
# print(z) # ma sie wypisac: x=100, y=50
# z.obroc_sie(90)
# z.idz(50)
# print(z) # ma sie wypisac: x=150, y=50
# ```

#ROZWIAZANIE
# Napisz klasę `Zolw` z metodami `idz` i `obroc_sie`. Żółw ma jakieś położenie (wyrażone dwiema współrzędnymi) i jakieś ustawienie, czyli kurs (wyznaczony pojedyncza liczba).

class Zolw:
    def __init__(self, pol_x: int, pol_y):
        self.pol_x = pol_x
        self.pol_y = pol_y
        self.kierunek = 0

    def get_info(self) ->str:
        return f'Polozenie ({self.pol_x}, {self.pol_y}), kierunek {self.kierunek}'

    def __str__(self) -> str:
        return self.get_info()

    # Metoda `obroc_sie ` powoduje obrót żółwia, czyli zmianę jego kursu.
    def obroc_sie(self, obroc_sie: int):
        obroty = [0, 90, 180, 270, 360]
        for obrot in obroty:
            if obroc_sie == obrot:
                self.kierunek =  self.kierunek + obroc_sie
                if self.kierunek >= 360:
                    self.kierunek = self.kierunek - 360
                    return self.kierunek
                else:
                    return self.kierunek

        else:
            raise ValueError(f'Zła wartość obrotu')

    # Metoda `idz` powoduje przejście żółwia o określoną odległość.
    def idz(self,idz: int):
        if self.kierunek == 0:
            self.pol_y -= idz
        if self.kierunek == 90:
            self.pol_x += idz
        if self.kierunek == 180:
            self.pol_y += idz
        if self.kierunek == 270:
            self.pol_x -= idz
        return self.pol_x, self.pol_y, self.kierunek

# z = Zolw(100, 100)
# z.idz(50)
# print(z) # ma sie wypisac: x=100, y=50
# z.obroc_sie(90)
# z.idz(50)
# print(z) # ma sie wypisac: x=150, y=50

z = Zolw(100,100)
z.idz(50)
print(z)
z.obroc_sie(90)
z.idz(50)
print(z)

