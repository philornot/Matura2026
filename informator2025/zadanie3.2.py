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
n = len(dane)
# print(dane)

wystepowania = [0]*n
dlugosc_maks = 0
for d in dane:
    a, b = d
    dlugosc = oblicz_dlugosc_przedzialu(a, b)
    wystepowania[dlugosc] += 1
    if wystepowania[dlugosc] == max(wystepowania):
        dlugosc_maks = dlugosc

print(dlugosc_maks)
print(f'({max(wystepowania)} razy)')