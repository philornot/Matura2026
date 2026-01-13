def wczytaj_plansze(przyklad=False):
    if przyklad:
        plik = "../Dane_2203/szachy_przyklad.txt"
        liczba_planszy = 9
    else:
        plik = "../Dane_2203/szachy.txt"
        liczba_planszy = 125
    with open(plik) as f:
        dane = f.read()

    szachownice = []
    plansza = []
    rzad = []
    for pole in dane:
        if pole.lower() in 'kwshgp.':
            rzad.append(pole)
        elif len(rzad) == 8:
            plansza.append(rzad)
            rzad = []
        else:  # pusta linia
            szachownice.append(plansza)
            plansza = []
            rzad = []

    # po pętli zostaje jeszcze jedna plansza
    szachownice.append(plansza)

    return szachownice, liczba_planszy


# plansze = wczytaj_plansze(przyklad=False)
# for plansza in plansze:
#     for wiersz in plansza:
#         print(wiersz)
#     print()

plansze, liczba_planszy = wczytaj_plansze(przyklad=False)

puste_kol_na_planszy = []
numer_planszy = 0
for plansza in plansze:
    numer_planszy += 1
    if numer_planszy > liczba_planszy:
        break

    l_pustych_kol_na_planszy = 0
    for i in range(8):
        pusta_kolumna = True
        for j in range(8):
            if plansza[j][i] != '.':
                pusta_kolumna = False
        if pusta_kolumna:
            l_pustych_kol_na_planszy += 1
    puste_kol_na_planszy.append(l_pustych_kol_na_planszy)

l_plansz_z_pustymi = 0
for i in puste_kol_na_planszy:
    if i != 0:
        l_plansz_z_pustymi += 1

max_l_pustych_na_planszy = max(puste_kol_na_planszy)

print(l_plansz_z_pustymi, max_l_pustych_na_planszy, sep=' ')
