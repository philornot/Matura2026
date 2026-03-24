def wczytaj_dane():
    with open('dane3.txt') as plik:
        dane_raw = plik.read().strip().split('\n')
    dane = []
    for d in dane_raw:
        d1, d2 = d.split()
        dane.append((int(d1), int(d2)))
    return dane


def oblicz_dlugosc_przedzialu(a, b):
    return b - a + 1


dane = wczytaj_dane()
# print(dane)

najmniejsza = 999999999
druga_najmniejsza = 999999999
for d in dane:
    a, b = d
    dlugosc = oblicz_dlugosc_przedzialu(a, b)
    if dlugosc < najmniejsza:
        druga_najmniejsza = najmniejsza
        najmniejsza = dlugosc
    elif dlugosc < druga_najmniejsza:
        druga_najmniejsza = dlugosc

print(najmniejsza, druga_najmniejsza)
