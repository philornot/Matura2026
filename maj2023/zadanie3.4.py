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


pi = wczytaj_pi(przyklad=False)


def czy_ciag_rosnaco_malejacy(ciag):
    if len(ciag) < 4:
        print('Ciąg jest za krótki')
        return -1

    indeks_podzialu = -2
    while indeks_podzialu > -len(ciag):
        lewy = ciag[:indeks_podzialu]
        prawy = ciag[indeks_podzialu:]

        if czy_rosnacy(lewy) and czy_malejacy(prawy):
            return True

        indeks_podzialu -= 1

    return False

def zamien_tablice_na_string(tablica):
    string = ''
    for i in tablica:
        string += str(i)
    return string

maks_dlugosc_ciagu = 0
maks_ciag = []
numer_wiersza = 0
for i in range(len(pi)):
    ciag = []
    for j in range(len(pi)):
        if len(ciag) > 4:
            if not czy_ciag_rosnaco_malejacy(ciag):
                if len(ciag) > maks_dlugosc_ciagu:
                    maks_dlugosc_ciagu = len(ciag) - 1  # bo ten ostatni, najnowszy, już psuje ciąg (?)
                    maks_ciag = zamien_tablice_na_string(ciag[:-1])
                    numer_wiersza = i + 1
                    break

        if i + j < len(pi):
            ciag.append(pi[i + j])

print(f'{numer_wiersza}\n'
      f'{maks_ciag}\n\n'
      f'(długość: {maks_dlugosc_ciagu})')