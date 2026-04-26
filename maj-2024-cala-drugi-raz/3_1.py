# 3332 --> 2


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


m = niep_skrot(3)
print(m)
