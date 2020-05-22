# Stwórz klasę `PlanszaXO` - jej obiekty mają reprezentować stan planszy do gry w kółko i krzyżyk.
# Ma ona mieć metody:
# `dodaj_element(x: int, y: int, rodzaj_elementu)`
# W argumencie `rodzaj_elementu` będzie napis `"x"` lub `"o"`. Jeśli ruch jest nieprawidłowy, metoda powinna zwracać fałsz.
# `stan_gry()`
# Ta metoda ma zwracać liczbę oznaczającą stan gry (gra trwa, gra zakończona sukcesem krzyżyków, gra zakończona sukcesem kółek).
# `czyj_ruch()`
# Ta metoda ma powiedzieć, czyj ruch ma być teraz (kółek czy krzyżyków).
# Wyświetlenie obiektu tej klasy ma wypisać planszę.
# Użyj tej klasy do zrobienia gry w kółko i krzyżyk.

class PlanszaXO:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def plansza():
        for i in range(1,4):
            print ([0,0,0])


x=PlanszaXO
x.plansza()
