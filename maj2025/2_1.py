def wczytaj_symbole(przyklad=False):
    if przyklad:
        plik = 'dane maj 23/symbole_przyklad.txt'
    else:
        plik = 'dane maj 23/symbole.txt'
    with open(plik) as f:
        return f.read().split()


symbole = wczytaj_symbole(przyklad=False)


def czy_palindrom(tekst):
    return tekst == tekst[::-1]


for symbol in symbole:
    if czy_palindrom(symbol):
        print(symbol)
