# Zadanie 1.9 FizzBuzz Napisz program, który wyświetla liczby od 1 do 100. Dla liczb podzielnych przez 3 niech
# program wyświetli `Fizz`; dla liczb podzielnych przez 5 niech wyświetli `Buzz`; a dla liczb podzielnych przez 15
# niech wyświetli `FizzBuzz`.

#ROZWIAZANIE

i = 1

while i<=100:
    if i % 15 == 0:
        print(f"{i}FizzBuzz")
        i+=1
    elif i % 3 == 0:
        print(f"{i}Fizz")
        i+=1
    elif i % 5 == 0:
        print(f"{i}Buzz")
        i+=1
    else:
        print(i)
        i+=1

