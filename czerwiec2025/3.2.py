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

n = len(dane)

wystapienia = {}
for znak in dane:
    if czy_cyfra(znak):
        wystapienia[znak] = 0

for znak in dane:
    if czy_cyfra(znak):
        wystapienia[znak] += 1

# print(wystapienia)

max_cyfa = ''
max_wyst = 0
for cyfra, wyst in wystapienia.items():
    if wyst > max_wyst:
        max_wyst = wyst
        max_cyfa = cyfra

print(max_cyfa, max_wyst, end=' ')