def wczytaj_dane():
    linie_clean = []
    with open('dane8.txt', 'r') as f:
        linie_raw = f.readlines()

    for linia_raw in linie_raw:
        linie_clean.append(int(linia_raw.strip()))

    return linie_clean


ciag = wczytaj_dane()
licznik = 0

for i in range(len(ciag)):
    for j in range(len(ciag)):
        if ciag[i] > ciag[j] and i < j:
            print(f'{ciag[i]} > {ciag[j]} oraz {i} < {j}')
            licznik += 1

print(f'\n\nWYNIK: {licznik}')
