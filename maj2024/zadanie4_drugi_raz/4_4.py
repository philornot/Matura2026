def wczytaj_liczby(przyklad=False):
    sciezka = 'liczby_przyklad.txt' if przyklad else 'liczby.txt'

    liczby = []
    with open(sciezka) as plik:
        for linia in plik:
            rzad = linia.split()
            rzad = [int(x) for x in rzad]
            liczby.append(rzad)
    return liczby


liczby = wczytaj_liczby(przyklad=False)[0]  # tylko pierwszy wiersz
# liczby = [i for i in range(1,101)]
print(liczby)

okno = []
maks_srednia = 0
maks_okno_start = 0
maks_okno_koniec = 50

for l_koniec in range(len(liczby) - 49):
    suma = sum(liczby[l_koniec:l_koniec + 50])

    for p_koniec in range(l_koniec + 50, len(liczby) + 1):
            dlugosc_okna = p_koniec - l_koniec
            srednia = suma / dlugosc_okna

            if srednia > maks_srednia:
                maks_srednia = srednia
                maks_okno_start = l_koniec
                maks_okno_koniec = p_koniec

            if p_koniec < len(liczby):
                suma += liczby[p_koniec]

print(f"{maks_srednia:.2f} {maks_okno_koniec - maks_okno_start} {liczby[maks_okno_start]}")