def wczytaj_dane(przyklad=False):
    if przyklad:
        plik = '../dane/odbiorcy_przyklad.txt'
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


# (w przykładzie 1. z wprowadzenia):
# odbiorcą komputera 4 jest odbiorcy[4 -1] = 3, dlatego komputer 4 zawsze będzie wysyłać do trzeciego
# odbiorcą dla komputera 1 jest odbiorcy[1 - 1] = 4, dlatego 1 zawsze wysyła do 4
# => odbiorcą dla komputera i jest odbiorcy[i - 1]

odbiorcy_test = [4, 3, 5, 3, 1, 2]
odbiorcy = wczytaj_dane(przyklad=False)
liczba_rund = 1
pakiety = runda(liczba_rund, odbiorcy)
for nr_pakietu, komputer in pakiety.items():
    print(f'[R{liczba_rund}] pakiet {nr_pakietu} w {komputer}')
