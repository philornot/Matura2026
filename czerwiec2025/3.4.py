def wczytaj_dane(przyklad=False):
    if przyklad:
        sciezka = 'dane_przyklad.txt'
    else:
        sciezka = 'dane.txt'
    with open(sciezka, 'r') as plik:
        return plik.read()


def czy_cyfra(znak):
    if len(znak) > 1:
        print('tylko 1 znak!!')
        return -1
    return '0' <= znak <= '9'


def czy_numer_telefonu(ciag_cyfr):
    if len(ciag_cyfr) != 9:
        return False
    for cyfra in ciag_cyfr:
        if not czy_cyfra(cyfra):
            return False
    return True


def policz_rozne_cyfry(ciag_znakow):
    wystepowania = {}
    for cyfra in ciag_znakow:
        wystepowania[cyfra] = 0
    for cyfra in ciag_znakow:
        wystepowania[cyfra] += 1

    return len(wystepowania.keys())


dane = wczytaj_dane(przyklad=False)

# print(dane)
# print(policz_rozne_cyfry('303004411'))

n = len(dane)

numery_telefonow = []
for i in range(n - 9):
    if not czy_cyfra(dane[i - 1]) and not czy_cyfra(dane[i + 9]):
        telefon = dane[i:(i + 9)]
        if czy_numer_telefonu(telefon):
            numery_telefonow.append(telefon)

min_rozne_cyfry = 11
min_telefony = []
for telefon in numery_telefonow:
    if policz_rozne_cyfry(telefon) < min_rozne_cyfry:
        min_telefony = [telefon]
        min_rozne_cyfry = policz_rozne_cyfry(telefon)
    elif policz_rozne_cyfry(telefon) == min_rozne_cyfry:
        min_telefony.append(telefon)


for tel in min_telefony:
    print(tel)
