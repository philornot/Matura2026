from wczytaj_dane import wczytaj_dane

liczby = wczytaj_dane(przyklad=False)


def nwd(a, b):
    while b:
        a, b = b, a % b
    return a


def nwd_z_listy(lista_liczb):
    wynik = lista_liczb[0]

    for i in lista_liczb[1:]:
        wynik = nwd(wynik, i)

    return wynik


ciag = []
maks_dlugosc_ciagu = 0
maks_ciag = []
maks_nwd = 0

for i in range(len(liczby)):
    ciag = [liczby[i]]

    for j in range(i + 1, len(liczby)):
        testowy_ciag = ciag + [liczby[j]]
        if nwd_z_listy(testowy_ciag) > 1:
            ciag.append(liczby[j])  # to wtedy dodaję do "prawdziwego"
        else:
            break

    if len(ciag) > maks_dlugosc_ciagu:
        maks_dlugosc_ciagu = len(ciag)
        maks_ciag = ciag
        maks_nwd = nwd_z_listy(ciag)

odp4_3 = f'pierwsza liczba ciągu {maks_ciag[0]}, długość {maks_dlugosc_ciagu}, największy wspólny dzielnik {maks_nwd}'
print(odp4_3)
with open('odp4-3.txt', 'w') as plik_wyjsciowy:
    plik_wyjsciowy.write(odp4_3)