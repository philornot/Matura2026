def wczytaj_symbole(przyklad=False):
    if przyklad:
        plik = 'dane maj 23/symbole_przyklad.txt'
    else:
        plik = 'dane maj 23/symbole.txt'
    with open(plik) as f:
        return f.read().split()


symbole = wczytaj_symbole(przyklad=False)


def czy_mozliwy_kwadrat(x, y, symbole):
    lewy_gorny = symbole[x][y]
    if len(symbole) - x < 3:
        return False
    if len(symbole[x]) - y < 3:
        return False

    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if symbole[i][j] != lewy_gorny:
                return False
    return True


def printuj_kwadrat(x, y, symbole):
    for j in range(y, y + 3):
        for i in range(x, x + 3):
            print(symbole[i][j], end='')
        print()


srodki = []
for x in range(len(symbole)):
    for y in range(len(symbole[x])):
        if czy_mozliwy_kwadrat(x, y, symbole):
            srodki.append((x + 2, y + 2))
            # printuj_kwadrat(x, y, symbole)

print(len(srodki), end=' ')
for srodek in srodki:
    x, y = srodek
    print(f'{x} {y}', end=' ')
