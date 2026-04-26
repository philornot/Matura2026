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

l1 = sorted(dane[0])
print(l1[-101])