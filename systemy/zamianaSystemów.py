def dec_na_szesnastkowy(liczba):
    if liczba == 0:
        return "0"
    cyfry = "0123456789ABCDEF"
    wynik = ""
    while liczba > 0:
        reszta = liczba % 16
        wynik = cyfry[reszta] + wynik
        liczba //= 16
    return wynik


def dec_na_siodemkowy(liczba):
    if liczba == 0:
        return "0"
    wynik = ""
    while liczba > 0:
        reszta = liczba % 7
        wynik = str(reszta) + wynik
        liczba //= 7
    return wynik


def szesnastkowy_na_dec(liczba):
    cyfry = "0123456789ABCDEF"
    liczba = liczba.upper()
    wynik = 0
    for znak in liczba:
        wartosc = 0
        for i in range(len(cyfry)):
            if cyfry[i] == znak:
                wartosc = i
                break
        wynik = wynik * 16 + wartosc
    return wynik


def siodemkowy_na_dec(s):
    wynik = 0
    for znak in s:
        wartosc = int(znak)
        wynik = wynik * 7 + wartosc
    return wynik
