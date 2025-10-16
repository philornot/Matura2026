plik = open('szachy.txt', 'r')


def szach(macierz):
    bialy_szachuje = False
    czarny_szachuje = False

    # Patrzymy wierszami
    for i in range(len(macierz)):
        for j in range(len(macierz)):
            if macierz[i][j] == 'W':
                for x in range(j + 1, len(macierz)):
                    if macierz[i][x] == '.':
                        continue
                    elif macierz[i][x] == 'k':
                        bialy_szachuje = True
                    break
                for x in range(j - 1, -1, -1):
                    if macierz[i][x] == '.':
                        continue
                    elif macierz[i][x] == 'k':
                        bialy_szachuje = True
                    break
            if macierz[i][j] == 'w':
                for x in range(j + 1, len(macierz)):
                    if macierz[i][x] == '.':
                        continue
                    elif macierz[i][x] == 'K':
                        czarny_szachuje = True
                    break
                for x in range(j - 1, -1, -1):
                    if macierz[i][x] == '.':
                        continue
                    elif macierz[i][x] == 'K':
                        czarny_szachuje = True
                    break
    # kolumny
    for j in range(len(macierz[0])):
        for i in range(len(macierz)):
            if macierz[i][j] == 'W':
                for x in range(i + 1, len(macierz)):
                    if macierz[x][j] == '.':
                        continue
                    elif macierz[x][j] == 'k':
                        bialy_szachuje = True
                    break
                for x in range(i - 1, -1, -1):
                    if macierz[x][j] == '.':
                        continue
                    elif macierz[x][j] == 'k':
                        bialy_szachuje = True
                    break

            if macierz[i][j] == 'w':
                for x in range(i + 1, len(macierz)):
                    if macierz[x][j] == '.':
                        continue
                    elif macierz[x][j] == 'K':
                        czarny_szachuje = True
                    break
                for x in range(i - 1, -1, -1):
                    if macierz[x][j] == '.':
                        continue
                    elif macierz[x][j] == 'K':
                        czarny_szachuje = True
                    break

    return bialy_szachuje, czarny_szachuje


tablica_macierzy = []
macierz = []
for wiersz in plik:
    wiersz = wiersz.strip()
    wiersz = list(wiersz)
    if len(wiersz) == 0:
        tablica_macierzy.append(macierz)
        macierz = []
    else:
        macierz.append(wiersz)

b = 0
c = 0
for macierz in tablica_macierzy:
    bialy, czarny = szach(macierz)
    if bialy == True:
        b += 1
    if czarny == True:
        c += 1

print(b, c)

plik.close()
