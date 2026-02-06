def wczytaj_pary():
    sciezka_do_pliku = '../Dane_2212/pary.txt'
    with open(sciezka_do_pliku) as plik:
        dane_raw = plik.read().split('\n')

    pary = []
    for para in dane_raw:
        if para.strip() == '':
            continue
        liczba1, liczba2 = para.split()
        pary.append((int(liczba1), int(liczba2)))

    return pary


def ile_strzalek(y, x):  # idąc od dołu drzewa
    while y > x:
        y = y // 2
    return y == x


pary = wczytaj_pary()
# print(pary)


licznik = 0
for para in pary:
    x, y = para
    if ile_strzalek(y, x) >= 1:
        print(x, y)
        licznik += 1
print(f'\nŁącznie {licznik} znalezionych par (wszystkich {len(pary)})')

# 47 3044
# 7650 61204
# 1 245
# 7 63669
# 9125 18250
# 5 43246
