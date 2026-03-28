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


dane = wczytaj_dane(przyklad=False)
# print(dane)

n = len(dane)

for i in range(n-9):
    if not czy_cyfra(dane[i-1]) and not czy_cyfra(dane[i+9]):
        telefon = dane[i:(i+9)]
        if czy_numer_telefonu(telefon):
            if telefon[0] == '5':
                # print(dane[(i-1):(i+10)])
                print(telefon)
