def wczytaj_dane():
    linie_clean = []
    with open('dane8.txt', 'r') as f:
        linie_raw = f.readlines()

    for linia_raw in linie_raw:
        linie_clean.append(int(linia_raw.strip()))

    return linie_clean


def luka(a, b):
    return abs(a - b)


ciag = wczytaj_dane()
luki_parzyste = 0
luki_nieparzyste = 0

for i in range(len(ciag)-1):
    if luka(ciag[i], ciag[i + 1]) % 2 == 0:
        luki_parzyste += 1
    else:
        luki_nieparzyste += 1

print(luki_parzyste, luki_nieparzyste)
