### Zadanie 2.2 | Choinka
# Napisz program, który wczytuje liczbę całkowitą, a następnie na konsolę wypisuje w tylu liniach "choinkę" ze znaków `*`. Np. dla parametru 3 powinno się wypisać:

# ```

#    *

#  * * *

# * * * * *

# ```

# ROZWIAZANIE

x = int(input("Wpisz liczbe: "))

for i in range(0, x*2):
        if i % 2 != 0:
            print(" "*round(x*2-i), "* "*i," "*round(x*2-i))
        else:
            print(" ")







