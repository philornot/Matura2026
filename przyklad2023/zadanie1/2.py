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


plansze, liczba_planszy = wczytaj_plansze(przyklad=False)

# for plansza in plansze:
#     for wiersz in plansza:
#         print(wiersz)
#     print()

numer_planszy = 0
licznik_plansz_w_rownowadze = 0
min_l_bierek_w_rownowadze = 65
for plansza in plansze:
    K = k = W = w = S = s = H = h = G = g = P = p = 0
    numer_planszy += 1
    if numer_planszy > liczba_planszy:
        break

    liczba_bierek = 0
    for i in range(8):
        for j in range(8):
            pole = plansza[i][j]
            if pole.lower() not in 'kwshgp':
                continue
            # najpierw nie doczytałem, że to mają być TAKIE SAME bierki, więc zrobiłem liczenie po kolorze
            # i jak się zorientowałem to już nie chciało mi się myśleć nad bardziej eleganckim rozwiązaniem
            if pole == 'K':
                K += 1
            if pole == 'k':
                k += 1
            if pole == 'W':
                W += 1
            if pole == 'w':
                w += 1
            if pole == 'S':
                S += 1
            if pole == 's':
                s += 1
            if pole == 'H':
                H += 1
            if pole == 'h':
                h += 1
            if pole == 'G':
                G += 1
            if pole == 'g':
                g += 1
            if pole == 'P':
                P += 1
            if pole == 'p':
                p += 1

            # może tak?
            # bierki = {'K': 0, 'k': 0, 'W': 0, 'w': 0, 'S': 0, 's': 0, 'H': 0, 'h': 0, 'G': 0, 'g': 0, 'P': 0, 'p': 0}
            # w każdym razie ten stos if-ów działa więc nie będę go ruszać :)

            liczba_bierek += 1

    if k == K and w == W and s == S and H == h and g == G and p == P:
        licznik_plansz_w_rownowadze += 1
        if liczba_bierek < min_l_bierek_w_rownowadze:
            min_l_bierek_w_rownowadze = liczba_bierek

print(licznik_plansz_w_rownowadze, min_l_bierek_w_rownowadze, sep=' ')
