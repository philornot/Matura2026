PLIK = 'Dane/gra.txt'
with open(PLIK) as f:
    plansza = f.read().splitlines()
N = len(plansza)
M = len(plansza[0])


def wczytaj_pierwsze_pokolenie():
    with open(PLIK) as f:
        plansza = f.read().splitlines()

    zyjace = set()  # zbiór współrzędnych (x, y) żyjących komórek
    for i, wiersz in enumerate(plansza):
        for j, komorka in enumerate(wiersz):
            if komorka == "X":
                zyjace.add((i, j))  # i - wiersz, j - kolumna
    return zyjace


def policz_zywych_sasiadow(zyjace, x, y):
    zywi_sasiedzi = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if i == x and j == y:
                continue
            if (i % N, j % M) in zyjace:
                zywi_sasiedzi += 1

    return zywi_sasiedzi


def symuluj_pokolenie(zyjace):  # n - wiersze, m - kolumny siatki
    nowe_zyjace = set()
    for i in range(N):
        for j in range(M):
            zyje = (i, j) in zyjace
            zywi_sasiedzi = policz_zywych_sasiadow(zyjace, i, j)

            if zyje and zywi_sasiedzi in [2, 3]:
                nowe_zyjace.add((i, j))
            elif not zyje and zywi_sasiedzi == 3:
                nowe_zyjace.add((i, j))
    return nowe_zyjace


def printuj_pokolenie(zyjace):
    for i in range(N):
        for j in range(M):
            if (i, j) in zyjace:
                print("X", end="")
            else:
                print(".", end="")
        print("\n", end='')


def k_pokolenie(k):  # zwraca k-te pokolenie
    zyjace = wczytaj_pierwsze_pokolenie()
    if k == 1:
        return zyjac

    nowe_zyjace = symuluj_pokolenie(zyjace)  # drugie pokolenie
    for i in range(k - 2):
        nowe_zyjace = symuluj_pokolenie(nowe_zyjace)

    return nowe_zyjace


# sprawdzenie
jedenaste_pok = k_pokolenie(11)
printuj_pokolenie(jedenaste_pok)
print(f"spr: liczba sąsiadów komórki (1,10) w 11. pokoleniu: {policz_zywych_sasiadow(jedenaste_pok, 1 - 1, 10 - 1)}")
print()

# 5.1
trzysiedem_pok = k_pokolenie(37)
print(f'[5.1] liczba sąsiadów dla komórki (2, 19) w 37. pokoleniu: {policz_zywych_sasiadow(trzysiedem_pok, 2 - 1, 19 - 1)}')
print("37. pokolenie:")
printuj_pokolenie(trzysiedem_pok)
print()

# 5.2
drugie_pok = k_pokolenie(2)
print(f'[5.2] Liczba żywych komórek w drugim pokoleniu: {len(drugie_pok)}')
print("2. pokolenie:")
printuj_pokolenie(drugie_pok)
print("")

# 5.3
zyjace = wczytaj_pierwsze_pokolenie()
poprzednie_zyjace = zyjace
for i in range(100):
    nowe_zyjace = symuluj_pokolenie(poprzednie_zyjace)
    if poprzednie_zyjace == nowe_zyjace:
        print(f'[5.3] Ustabilizowało się w {i-1} pokoleniu, liczba żywych: {len(poprzednie_zyjace)}')
        print(f"Pokolenie {i-1}:")
        printuj_pokolenie(poprzednie_zyjace)
        print(f"pokolenie {i}:")
        printuj_pokolenie(nowe_zyjace)
        break

    poprzednie_zyjace = nowe_zyjace
