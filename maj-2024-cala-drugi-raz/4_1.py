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

l1, l2 = dane[0], dane[1]
licznik = 0
for liczba1 in l1:
    for liczba2 in l2:
        if liczba2 % liczba1 == 0:
            licznik += 1
            break

print(licznik)