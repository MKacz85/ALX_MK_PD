# Zadanie 1.3 | Współczynnik BMI (ok. 2 godz.)
# Napisz program, który dla podanych liczb: wzrostu w cm i masy ciała w
# kg obliczą i wypisze współczynnik BMI, oraz podsumowanie informujące o stanie/zaleceniach. (Informacje o BMI: wzór,
# interpretację wyników, proszę znaleźć samodzielnie).

# ROZWIAZANIE

waga = float(input("Podaj swoja mase ciala (w kg): "))
wzrost = float(input("Podaj swoj wzrost (w cm): "))

BMI = waga/(wzrost/100)**2

if BMI < 16:
    print(f"Twoj BMI wynosi {BMI:.2f}, jestes wyglodzony.")
elif 16 < BMI < 16.99:
    print(f"Twoj BMI wynosi {BMI:.2f}, jestes wychodzony.")
elif 17 < BMI < 18.49:
    print(f"Twoj BMI wynosi {BMI:.2f}, masz niedowage.")
elif 18.5 < BMI < 24.99:
    print(f"Twoj BMI wynosi {BMI:.2f}, masz pozadana mase ciałą.")
elif 25 < BMI < 29.99:
    print(f"Twoj BMI wynosi {BMI:.2f}, masz nadwage.")
elif 30 < BMI < 34.99:
    print(f"Twoj BMI wynosi {BMI:.2f}, masz otylosc I stopnia.")
elif 35 < BMI < 39.99:
    print(f"Twoj BMI wynosi {BMI:.2f}, masz otylosc II stopnia.")
elif 40 <= BMI:
    print(f"Twoj BMI wynosi {BMI:.2f}, masz otylosc III stopnia.")
