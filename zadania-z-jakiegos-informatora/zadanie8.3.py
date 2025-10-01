def wczytaj_dane():
    linie_clean = []
    with open('dane8.txt', 'r') as f:
        linie_raw = f.readlines()

    for linia_raw in linie_raw:
        linie_clean.append(int(linia_raw.strip()))

    return linie_clean


ciag = wczytaj_dane()
dlugosc_podciagu = 1
maks_podciag = 0

for i in range(len(ciag) - 1):
    if ciag[i] < ciag[i + 1]:
        dlugosc_podciagu += 1
    else:
        dlugosc_podciagu = 1

    if dlugosc_podciagu > maks_podciag:
        maks_podciag = dlugosc_podciagu

print(maks_podciag)
