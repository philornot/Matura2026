def dlugosc_liczby(liczba):
    dlugosc = 0
    while liczba > 0:
        dlugosc += 1
        liczba = liczba // 10
    return dlugosc


def odwroc_pary_cyfr(liczba):
    if liczba == 0:
        return 0

    liczba_cyfr = dlugosc_liczby(liczba)

    dzielnik = 1
    for i in range(liczba_cyfr - 1):  # oblicz największą potęgę
        dzielnik = dzielnik * 10

    wynik = 0

    while dzielnik > 0:
        if dzielnik >= 10:  # zostały przynajmniej 2 cyfry
            cyfra1 = liczba // dzielnik
            liczba = liczba % dzielnik
            dzielnik //= 10

            cyfra2 = liczba // dzielnik
            liczba = liczba % dzielnik
            dzielnik //= 10

            wynik = wynik * 100 + cyfra2 * 10 + cyfra1
        else:  # została jedna cyfra
            cyfra1 = liczba // dzielnik
            wynik = wynik * 10 + cyfra1
            dzielnik = 0

    return wynik


l = int(input('liczba='))
print(odwroc_pary_cyfr(l))
