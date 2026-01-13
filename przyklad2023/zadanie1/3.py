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
def czy_biala_wieza_szachuje_czarnego_krola(plansza):
    szach = False
    for i in range(8):
        for j in range(8):
            pole = plansza[i][j]
            if pole == 'k':
                for w in range(j + 1, 8):
                    if plansza[i][w] == 'W':
                        szach = True
                        break
                    if plansza[i][w] != '.':
                        break  # nie szachuje w wierszu po prawej

                for w in range(j - 1, -1, -1):
                    if plansza[i][w] == 'W':
                        szach = True
                        break
                    if plansza[i][w] != '.':
                        break  # nie szachuje w wierszu po lewej

                for k in range(i + 1, 8):
                    if plansza[k][j] == 'W':
                        szach = True
                        break
                    if plansza[k][j] != '.':
                        break  # nie szachuje w kolumnie od góry

                for k in range(i - 1, -1, -1):
                    if plansza[k][j] == 'W':
                        szach = True
                        break
                    if plansza[k][j] != '.':
                        break  # nie szachuje w kolumnie od dołu

    return szach


def czy_czarna_wieza_szachuje_bialego_krola(plansza):
    szach = False
    for i in range(8):
        for j in range(8):
            pole = plansza[i][j]
            if pole == 'K':

                for w in range(j + 1, 8):
                    if plansza[i][w] == 'w':
                        szach = True
                        break
                    if plansza[i][w] != '.':
                        break  # nie szachuje w wierszu po prawej

                for w in range(j - 1, -1, -1):
                    if plansza[i][w] == 'w':
                        szach = True
                        break
                    if plansza[i][w] != '.':
                        break  # nie szachuje w wierszu po lewej

                for k in range(i + 1, 8):
                    if plansza[k][j] == 'w':
                        szach = True
                        break
                    if plansza[k][j] != '.':
                        break  # nie szachuje w kolumnie od góry

                for k in range(i - 1, -1, -1):
                    if plansza[k][j] == 'w':
                        szach = True
                        break
                    if plansza[k][j] != '.':
                        break  # nie szachuje w kolumnie od dołu
    return szach


plansze, liczba_planszy = wczytaj_plansze(przyklad=False)

numer_planszy = 0
biala_szach = czarna_szach = 0
for plansza in plansze:
    numer_planszy += 1
    if numer_planszy > liczba_planszy:
        break

    if czy_biala_wieza_szachuje_czarnego_krola(plansza):
        biala_szach += 1
        print('\nBiała wieża szachuje czarnego króla:')
        for wiersz in plansza:
            print(wiersz)
        print()
    if czy_czarna_wieza_szachuje_bialego_krola(plansza):
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
