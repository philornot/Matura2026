def wczytaj_dane(przyklad=False):
    sciezka_do_pliku = 'Dane/przyklad_zegar_binarny.txt' if przyklad else 'Dane/zegar_binarny.txt'
    with open(sciezka_do_pliku, 'r') as plik:
        linie = plik.readlines()
    godziny = []
    for linia in linie:
        godziny.append(linia.split())
    return godziny


def zamien_godzine_na_dec(godzina_bin):
    godzina_dec = []
    for liczba_bin in godzina_bin:
        godzina_dec.append(int(liczba_bin, 2))

    return f'{godzina_dec[0]}{godzina_dec[1]}:{godzina_dec[2]}{godzina_dec[3]}:{godzina_dec[4]}{godzina_dec[5]}'


godziny_bin = wczytaj_dane(przyklad=False)
znalezione_godziny = []
for godzina_bin in godziny_bin:
    godzina_dec = zamien_godzine_na_dec(godzina_bin).split(':')
    minuty = godzina_dec[1]
    sekundy = godzina_dec[2]
    if minuty == sekundy:
        znalezione_godziny.append(godzina_bin)

for godzina_bin in znalezione_godziny:
    for i in godzina_bin:
        print(i, end=' ')
    print()
