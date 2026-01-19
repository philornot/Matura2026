def wczytaj_dane(przyklad=False):
    if przyklad == True:
        plik = '../dane/odbiorcy_przyklad.txt'
    elif przyklad == 'test':
        return [4, 3, 5, 3, 1, 2]
    else:
        plik = '../dane/odbiorcy.txt'
    with open(plik, 'r') as f:
        raw = f.read().split()

    dane = []
    for i in raw:
        dane.append(int(i))
    return dane


def runda(nr_rundy, odbiorcy):
    # Pierwsza runda
    n = len(odbiorcy)
    pakiety = {}
    for i in range(n):
        nr_pakietu = i + 1
        pakiety[nr_pakietu] = odbiorcy[i]

    # kolejne rundy
    for i in range(nr_rundy - 1):
        for nr_pakietu, komputer in pakiety.items():
            pakiety[nr_pakietu] = odbiorcy[komputer - 1]
    return pakiety


def najwieksza_liczba_pakietow_ktore_trafiaja_do_jednego_komputera(nr_rundy, odbiorcy):
    pakiety = runda(nr_rundy, odbiorcy)
    komputery = {}
    for numer_pakietu, komputer in pakiety.items():
        if komputer not in komputery.keys():
            komputery[komputer] = [numer_pakietu]
        else:
            komputery[komputer].append(numer_pakietu)

    # print(komputery)

    maks = 0
    for komputer, numery_pakietu in komputery.items():
        if len(numery_pakietu) > maks:
            maks = len(numery_pakietu)

    return maks


# najwieksza_liczba_pakietow_ktore_trafiaja_do_jednego_komputera(6, odbiorcy=wczytaj_dane(przyklad='test'))

odbiorcy = wczytaj_dane(przyklad=False)
for i in [1, 2, 4, 8]:
    print(najwieksza_liczba_pakietow_ktore_trafiaja_do_jednego_komputera(i, odbiorcy), end=' ')
