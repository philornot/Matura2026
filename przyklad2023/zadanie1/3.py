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
def czy_biala_wieza_szachuje_czarnego_krola(plansza, numer=0):
    szach = False
    for i in range(8):
        for j in range(8):
            pole = plansza[i][j]
            if pole == 'k':
                for w in range(j, -1):
                    if plansza[i][w] not in ['.', 'k', 'W']:
                        break  # nie szachuje w wierszu po prawej
                    szach = True

                for w in range(-1, j - 1):
                    if plansza[i][w] not in ['.', 'k', 'W']:
                        break  # nie szachuje w wierszu po lewej
                    szach = True

                for k in range(i, -1):
                    if plansza[k][j] not in ['.', 'k', 'W']:
                        break  # nie szachuje w kolumnie od góry
                    szach = True

                for k in range(-1, i - 1):
                    if plansza[k][j] not in ['.', 'k', '1W']:
                        break  # nie szachuje w kolumnie od dołu
                    szach = True

    return szach


def czy_czarna_wieza_szachuje_bialego_krola(plansza, numer=0):
    szach = False
    for i in range(8):
        for j in range(8):
            pole = plansza[i][j]
            if pole == 'K':

                for w in range(j, -1):
                    if plansza[i][w] not in ['.', 'K', 'w']:
                        break  # nie szachuje w wierszu po prawej
                    szach = True
                for w in range(-1, j - 1):
                    if plansza[i][w] not in ['.', 'K', 'w']:
                        break  # nie szachuje w wierszu po lewej
                    szach = True

                for k in range(i, -1):
                    if plansza[k][j] not in ['.', 'K', 'w']:
                        break  # nie szachuje w kolumnie od góry
                    szach = True

                for k in range(-1, i - 1):
                    if plansza[k][j] not in ['.', 'K', 'w']:
                        break  # nie szachuje w kolumnie od dołu
                    szach = True
    return szach


plansze, liczba_planszy = wczytaj_plansze(przyklad=True)

numer_planszy = 0
biala_szach = czarna_szach = 0
for plansza in plansze:
    numer_planszy += 1
    if numer_planszy > liczba_planszy:
        break

    if czy_biala_wieza_szachuje_czarnego_krola(plansza, numer=numer_planszy):
        biala_szach += 1
        print('\nBiała wieża szachuje czarnego króla:')
        for wiersz in plansza:
            print(wiersz)
        print()
    if czy_czarna_wieza_szachuje_bialego_krola(plansza, numer=numer_planszy):
        czarna_szach += 1
        print('\nCzarna wieża szachuje białego króla')
        for wiersz in plansza:
            print(wiersz)
        print()

print(biala_szach, czarna_szach, sep=' ')

# wk....W.
# ........
# .W.....k
# ....s...
# ....S...
# ......k.
# ........
# ......p.
