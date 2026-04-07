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


godziny = wczytaj_dane(przyklad=False)
licznik = 0
znalezione_wiersze = ''
for i, godzina_bin in enumerate(godziny):
    godzina_dec = zamien_godzine_na_dec(godzina_bin)
    # print(godzina_bin, godzina_dec)
    if godzina_dec == '17:22:14':
        licznik += 1
        znalezione_wiersze += f'{i + 1} '

print(licznik)
print(znalezione_wiersze)
