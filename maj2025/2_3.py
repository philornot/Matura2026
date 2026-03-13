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


maks = 0
maks_symbol = ''
for symbol in symbole:
    liczba = symbol_na_dec(symbol)
    if liczba > maks:
        maks = liczba
        maks_symbol = symbol

print(f'{maks} {maks_symbol}')
