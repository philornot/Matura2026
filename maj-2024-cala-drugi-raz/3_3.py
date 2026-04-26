def wczytaj_dane(przyklad=False):
    sciezka = 'skrot2_przyklad.txt' if przyklad else 'skrot2.txt'
    with open(sciezka, 'r') as plik:
        raw = plik.read().split()
        return [int(i) for i in raw]

def niep_skrot(n):
    # print(f'liczba={n}')
    liczba = n
    m = 0
    ostatnia = liczba % 10
    i = 0
    nieparzyste = {}
    while liczba > 0:
        while ostatnia % 2 == 0:
            # print(f'{ostatnia} jest parzysta')
            liczba = liczba // 10
            ostatnia = liczba % 10
            # print(f'liczba po podzieleniu przez 10: {liczba}, ostatnia={ostatnia}')
            if liczba // 10 == 0 and ostatnia == 0:
                if i == 0:
                    return False
                else:
                    break

        nieparzyste[i] = ostatnia * (10 ** i)
        # print(f'{ostatnia} nie jest parzysta, dzielę przez 10')
        liczba = liczba // 10
        ostatnia = liczba % 10
        # print(f'liczba={liczba}, ostatnia={ostatnia}, nieparzyste={nieparzyste}')
        i += 1

    for i in nieparzyste:
        m += nieparzyste[i]

    return m

def nwd(a, b):
    while b:
        a, b = b, a % b
    return a

dane = wczytaj_dane(przyklad=False)
#print(dane)

licznik = 0
maks = 0
for i in dane:
    skrot = niep_skrot(i)
    if nwd(i, niep_skrot(i)) == 7:
        print(i)