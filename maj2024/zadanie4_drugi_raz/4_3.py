def wczytaj_liczby(przyklad=False):
    sciezka = 'liczby_przyklad.txt' if przyklad else 'liczby.txt'

    liczby = []
    with open(sciezka) as plik:
        for linia in plik:
            rzad = linia.split()
            rzad = [int(x) for x in rzad]
            liczby.append(rzad)
    return liczby


def rozklad_na_dzielniki(liczba):
    dzielniki = []
    n = 2
    while liczba > 1:
        if liczba % n == 0:
            dzielniki.append(n)
            liczba //= n
        else:
            n += 1
    return dzielniki


def policz_wyst_elementow(lista):
    wystapienia = {}
    for element in lista:
        if element not in wystapienia:
            wystapienia[element] = 1
        else:
            wystapienia[element] += 1
    return wystapienia


liczby = wczytaj_liczby(przyklad=False)
wiersz1, wiersz2 = liczby
wystapienia1 = policz_wyst_elementow(wiersz1)
odpowiedz = []

# print(wystapienia1)
# print(wiersz1)
# print(wiersz2)
# print(rozklad_na_dzielniki(48))

for liczba in wiersz2:
    rozklad = rozklad_na_dzielniki(liczba)
    wystapienia_rozklad = policz_wyst_elementow(rozklad)
    ok = False
    for l, w in wystapienia_rozklad.items():
        if l not in wystapienia1:
            ok = False
        elif wystapienia1[l] >= w:
            ok = True
            if liczba not in odpowiedz:
                odpowiedz.append(liczba)

for l in odpowiedz:
    print(l, end=' ')