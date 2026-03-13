def wczytaj_symbole(przyklad=False):
    if przyklad:
        plik = 'dane maj 23/symbole_przyklad.txt'
    else:
        plik = 'dane maj 23/symbole.txt'
    with open(plik) as f:
        return f.read().split()


symbole = wczytaj_symbole(przyklad=False)


def symbol_na_dec(symbol):
    trojkowy = {"o": '0', "+": '1', "*": '2'}
    liczba = ''
    for s in symbol:
        liczba = liczba + trojkowy[s]
    return int(liczba, 3)


def dec_na_trojk(liczba_dec):
    liczba_trojk = ''
    while liczba_dec > 0:
        reszta = liczba_dec % 3
        liczba_trojk = str(reszta) + liczba_trojk
        liczba_dec //= 3
    return liczba_trojk


suma = 0
for symbol in symbole:
    suma += symbol_na_dec(symbol)

trojkowy_odwrocony = {"0": "o", "1": "+", "2": "*"}

suma_trojkowa = dec_na_trojk(suma)
suma_w_znakach = ''
for cyfra in suma_trojkowa:
    suma_w_znakach = suma_w_znakach + trojkowy_odwrocony[cyfra]

print(f'{suma} {suma_w_znakach}')
