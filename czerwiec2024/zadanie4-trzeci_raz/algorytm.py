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


odbiorcy = wczytaj_dane(przyklad=True)


# print(odbiorcy)


# odbiorcy[nr_komputera] = nr_komputera_ktory_odbiera_pakiet
# {nr_komputera : nr_komputera_ktory_odbiera_pakiet}

# pakiety[numer_pakietu] = komputer_w_ktorym_jest_ten_pakiet
# {numer_pakietu : komputer_w_ktorym_jest_ten_pakiet}

# komputery[nr_pakietu] = numer_komputera
# {nr_pakietu : numer_komputera}

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


test_odbiorcy = [4, 3, 5, 3, 1, 2]
# print(test_odbiorcy)
for i in range(1, 7):
    print(i, runda(test_odbiorcy, i))
