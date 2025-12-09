def szyfruj(TekstJ, N):
    tabela = []
    for i in range(N):
        tabela.append([''] * N)

    i = 0
    for wier in range(N):
        for kol in range(N):
            if i > len(TekstJ):
                break
            tabela[wier][kol] = TekstJ[i]
            i += 1

    TekstZ = ''

    licznik = 0
    for i in range(N):
        for j in range(N):
            TekstZ = TekstZ + tabela[j][i]
            licznik += 1

    while licznik < len(TekstJ):
        TekstZ = TekstZ + 'X'
        licznik += 1

    return TekstZ

print(szyfruj('Czytanie książek to najpiękniejsza zabawa, jaką sobie ludzkość wymyśliła.',4))