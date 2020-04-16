# Zadanie 1.2 | Buty do szewca (ok. 1 godz.)
# Napisz taki program: użytkownik ma podać, w jaki dzień tygodnia oddał
# buty do szewca (poniedziałek to dzień 1, wtorek to dzień 2 itp.). Ma też podać, ile dni będzie trwała naprawa.
# Program ma wypisać, w jaki dzień tygodnia buty będą gotowe do odbioru. Jeśli tak będzie ci wygodniej,
# możesz założyć, że naprawa butów nigdy nie będzie trwała dłużej niż siedem dni.

# ROZWIAZANIE

while True:
    dzien_tygodnia = int(input("Podaj numer dnia tygodnia (gdzie 1 - poniedzialek a 7 - niedziela), w ktorym oddales/as buty do szewca?: "))
    if dzien_tygodnia < 1 or dzien_tygodnia > 7:
        print(f"Niepoprawny dzien tygodnia")
        continue

    czas_naprawy = int(input("Podaj czas naprawy butow(ile dni zajmie naprawa)?: "))

    numer_dnia_odbioru = dzien_tygodnia + czas_naprawy - 7

    dzien_odbioru = None

    if numer_dnia_odbioru == 1:
        dzien_odbioru = "poniedzialek"
    elif numer_dnia_odbioru == 2:
        dzien_odbioru  = "wtorek"
    elif numer_dnia_odbioru == 3:
        dzien_odbioru = "sroda"
    elif numer_dnia_odbioru == 4:
        dzien_odbioru = "czwartek"
    elif numer_dnia_odbioru == 5:
        dzien_odbioru = "piatek"
    elif dzien_odbioru == 6:
        dzien_odbioru = "sobota"
    else:
        dzien_odbioru = "niedziela"

    print(f"Twoje buty sa do odebrania w {dzien_odbioru} nastepnego tygodnia.")
    break






