def wczytaj_dane(przyklad=False, czy_inty=True):
    sciezka = 'przyklad.txt' if przyklad else 'liczby.txt'
    with open(sciezka, 'r') as plik:
        liczby_str = plik.read().split()
    if czy_inty:
        return [int(liczba) for liczba in liczby_str]
    else:
        return liczby_str


def czy_trojka_jest_dobra(x, y, z):
    if x == y or x == z or y == z:
        return False

    if y % x != 0 or z % y != 0:
        return False

    return True


def czy_piatka_jest_dobra(u, w, x, y, z):
    if u in [w, x, y, z] or w in [u, x, y, z] or x in [u, w, y, z] or y in [u, w, x, z] or z in [u, w, x, y]:
        return False

    if w % u != 0 or x % w != 0 or y % x != 0 or z % y != 0:
        return False

    return True


liczby = wczytaj_dane(przyklad=False)
# print(liczby)
# print(czy_trojka_jest_dobra(2,6,12))
# print(czy_trojka_jest_dobra(2,10,12))

licznik_trojek = licznik_piatek = 0
n = len(liczby)
for i in range(n):
    x = liczby[i]
    for j in range(n):
        y = liczby[j]
        for k in range(n):
            z = liczby[k]

            if czy_trojka_jest_dobra(x, y, z):
                licznik_trojek += 1
                print(x, y, z)
                with open('trojki.txt', 'a') as plik:
                    plik.write(f'{x} {y} {z}\n')

            # for l in range(n):
            #     u = liczby[l]
            #     for m in range(n):
            #         w = liczby[m]
            #
            #         if czy_piatka_jest_dobra(u, w, x, y, z):
            #             licznik_piatek += 1
            #             print(u, w, x, y, z)


print(f'\na) {licznik_trojek}')
print(f'\nb) {licznik_piatek}')