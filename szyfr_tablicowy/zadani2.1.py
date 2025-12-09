def zapisz_w_tabeli(tekst, N):
    tabela = []
    for i in range(N):
        tabela.append([''] * N)

    i = 0
    for wier in range(N):
        for kol in range(N):
            if i > len(tekst):
                break
            tabela[wier][kol] = tekst[i]
            i += 1
    return tabela


def szyfruj(tekst, N):
    tabela = zapisz_w_tabeli(tekst, N)
    szyfr = ''
    N = len(tabela[0])
    licznik = 0
    for i in range(N):
        for j in range(N):
            szyfr = szyfr + tabela[j][i]
            licznik += 1
    while licznik < len(tekst):
        szyfr = szyfr + 'X'
        licznik += 1
    return szyfr


tekst = "Czytanie książek to najpiękniejsza zabawa, jaką sobie ludzkość wymyśliła."
N = 4

szyfr = szyfruj(tekst, N)

print(szyfr)
