def wczytaj_dane(przyklad=False, czy_inty=True):
    sciezka = 'przyklad.txt' if przyklad else 'liczby.txt'
    with open(sciezka, 'r') as plik:
        liczby_str = plik.read().split()
    if czy_inty:
        return [int(liczba) for liczba in liczby_str]
    else:
        return liczby_str


def rozklad_na_czynniki_pierwsze(liczba):
    czynniki = []
    for n in range(2, liczba+1):
        while liczba % n == 0:
            czynniki.append(n)
            liczba //= n
        else:
            n += 1
    return czynniki


liczby = wczytaj_dane(przyklad=False)

maks_czynnikow = maks_roznych = liczba_z_maks_czynnikow = liczba_z_maks_roznych = 0
for liczba in liczby:
    wystepowanie = {}
    rozklad = rozklad_na_czynniki_pierwsze(liczba)

    for czynnik in rozklad:
        if czynnik not in wystepowanie:
            wystepowanie[czynnik] = 1
        else:
            wystepowanie[czynnik] += 1

    liczba_roznych_czynnikow = len(wystepowanie.keys())
    liczba_czynnikow = len(rozklad)

    if liczba_roznych_czynnikow > maks_roznych:
        maks_roznych = liczba_roznych_czynnikow
        liczba_z_maks_roznych = liczba

    if liczba_czynnikow > maks_czynnikow:
        maks_czynnikow = liczba_czynnikow
        liczba_z_maks_czynnikow = liczba


print(liczba_z_maks_czynnikow, maks_czynnikow, liczba_z_maks_roznych, maks_roznych)