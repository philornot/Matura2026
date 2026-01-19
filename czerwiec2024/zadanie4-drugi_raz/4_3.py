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


odbiorcy = wczytaj_dane(przyklad=False)
odbiorcy_przyklad1 = [4, 3, 5, 3, 1, 2]

# odbiorcy = odbiorcy_przyklad1
n = len(odbiorcy)

# pierwsza runda
pakiety = {}
for i in range(n):
    nr_pakietu = i + 1
    pakiety[nr_pakietu] = odbiorcy[i]

znalezione_pakiety = []
nr_rundy = 0
while not znalezione_pakiety:
    nr_rundy += 1

    pakiety = runda(nr_rundy, odbiorcy)

    for nr_p in pakiety.keys():
        if pakiety[nr_p] == nr_p:
            # print(nr_rundy, nr_p)
            znalezione_pakiety.append(nr_p)

min_szukany_pakiet = min(znalezione_pakiety)
szukana_runda = nr_rundy

print(szukana_runda, min_szukany_pakiet)
