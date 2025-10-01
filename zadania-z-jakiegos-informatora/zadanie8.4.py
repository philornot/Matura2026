def wczytaj_dane():
    linie_clean = []
    with open('dane8.txt', 'r') as f:
        linie_raw = f.readlines()

    for linia_raw in linie_raw:
        linie_clean.append(int(linia_raw.strip()))

    return linie_clean


ciag = wczytaj_dane()
n = len(ciag)
dlugosc_podciagu = [1] * n

for i in range(n):
    for j in range(i):
        if ciag[j] < ciag[i]:
            if dlugosc_podciagu[j] + 1 > dlugosc_podciagu[i]:
                dlugosc_podciagu[i] = dlugosc_podciagu[j] + 1

maksymalna_dlugosc = 0
for dlugosc in dlugosc_podciagu:
    if dlugosc > maksymalna_dlugosc:
        maksymalna_dlugosc = dlugosc

print(maksymalna_dlugosc)
