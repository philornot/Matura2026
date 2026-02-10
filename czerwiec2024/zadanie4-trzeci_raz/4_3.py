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


def runda(odbiorcy, numer_rundy):
    # pierwsza runda (zerowa?)
    n = len(odbiorcy)
    pakiety = {}
    for i in range(n):
        nr_pakietu = i + 1
        pakiety[nr_pakietu] = odbiorcy[i]

    # kolejne rundy
    for i in range(numer_rundy - 1):
        for nr_pakietu, komputer in pakiety.items():
            pakiety[nr_pakietu] = odbiorcy[komputer - 1]
    return pakiety


odbiorcy = wczytaj_dane(przyklad=True)
rundy = []
for i in range(10):
    pakiety = runda(odbiorcy, numer_rundy=i+1)
    rundy.append(pakiety)
for nr_rundy, r in enumerate(rundy):
    print(nr_rundy+1, r)