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


dane = wczytaj_dane(przyklad=False)
# print(dane)

licznik = 0
for i in range(len(dane)):
    znak = dane[i]
    if znak == '0':
        if dane[i-1] == '5' and not czy_cyfra(dane[i-2]):
            # print(dane[(i-2):(i+20)])
            licznik += 1


print(licznik)