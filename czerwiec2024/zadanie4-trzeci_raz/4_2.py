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


odbiorcy = wczytaj_dane(przyklad=False)
licznik = 0
for i in range(1, len(odbiorcy) + 1):
    if i not in odbiorcy:
        licznik += 1

print(licznik)
