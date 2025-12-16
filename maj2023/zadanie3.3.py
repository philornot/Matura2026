def wczytaj_pi(przyklad=False):
    if przyklad:
        plik = 'pi_przyklad.txt'
    else:
        plik = 'pi.txt'
    with open(plik, 'r') as f:
        dane = f.read().split()
    pi = []
    for i in range(len(dane)):
        pi.append(int(dane[i]))
    return pi


def czy_rosnacy(ciag):
    i = 0
    while i + 1 < len(ciag):
        if ciag[i] >= ciag[i + 1]:
            return False
        i += 1
    return True


def czy_malejacy(ciag):
    i = 0
    while i + 1 < len(ciag):
        if ciag[i] <= ciag[i + 1]:
            return False
        i += 1
    return True


# przyklad_ciag1 = [2, 5, 7, 9, 8, 3, 1]
# przyklad_ciag2 = [5, 9, 9, 4, 1]
# przyklad_ciag3 = [2, 5, 8, 4, 3, 4, 5]
# przyklad_ciag4 = [1, 2, 3, 4]
# przyklad_ciag5 = [5, 5, 3, 2, 1]

pi = wczytaj_pi(przyklad=False)
licznik = 0
for i in range(len(pi)):
    ciag = []
    for j in range(6):
        if i + j < len(pi):
            ciag.append(pi[i + j])

    if len(ciag) < 4:
        continue

    indeks_podzialu = -2
    while indeks_podzialu > -6:
        lewy = ciag[:indeks_podzialu]
        prawy = ciag[indeks_podzialu:]

        if czy_rosnacy(lewy) and czy_malejacy(prawy):
            licznik += 1
            print(ciag)

        indeks_podzialu -= 1

print(f'\nLicznik: {licznik}')
