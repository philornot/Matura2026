def wczytaj_dane(przyklad=False):
    if przyklad:
        plik = 'liczby_przyklad.txt'
    else:
        plik = 'liczby.txt'
    with open(plik, 'r') as f:
        wiersz1_raw, wiersz2_raw = f.readlines()
    wiersz1, wiersz2 = [], []
    wiersz1_raw, wiersz2_raw = wiersz1_raw.split(), wiersz2_raw.split()
    for i in wiersz1_raw:
        wiersz1.append(int(i))
    for j in wiersz2_raw:
        wiersz2.append(int(j))
    return wiersz1, wiersz2