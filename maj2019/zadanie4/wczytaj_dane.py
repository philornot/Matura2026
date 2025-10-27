def wczytaj_dane(przyklad=False):
    dane = []
    if przyklad:
        liczby = 'przyklad.txt'
    else:
        liczby = 'liczby.txt'

    with open(liczby, 'r') as plik:
        for linia in plik:
            dane.append(int(linia.strip()))

    return dane
