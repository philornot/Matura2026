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


odbiorcy = [3, 1, 6, 5, 4, 5]

for i in range(1, 7):
    print(i, runda(odbiorcy, i))
