def wczytaj_dane(przyklad=False):
    sciezka = 'liczby_przyklad.txt' if przyklad else 'liczby.txt'
    with open(sciezka, 'r') as plik:
        linie = plik.read().split('\n')
        if '' in linie:
            linie.remove('')
        dane = []
        for linia in linie:
            linia = linia.split()
            linia = [int(i) for i in linia]
            dane.append(linia)
        return dane


dane = wczytaj_dane(przyklad=False)
# for linia in dane:
#     print(linia)
liczby = dane[0]
maks_srednia = 0
maks_liczba_el = 0
maks_pierwszy_el = 0
maks_okno = []
for i in range(len(liczby)):
    okno = liczby[i:(i + 50)]
    srednia_arytmetyczna = sum(okno) / 50
    # print(srednia_arytmetyczna)
    if srednia_arytmetyczna > maks_srednia:
        maks_srednia = srednia_arytmetyczna
        maks_liczba_el = len(okno)
        maks_pierwszy_el = okno[0]
        maks_okno = okno

print(maks_srednia, maks_liczba_el, maks_pierwszy_el, sep=' ')
# print(maks_okno)