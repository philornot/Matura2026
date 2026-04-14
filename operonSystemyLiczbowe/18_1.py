def wczytaj_dane():
    sciezka = 'trzyliczby.txt'
    with open(sciezka, 'r') as plik:
        linie = plik.readlines()
    dane = []
    for linia in linie:
        liczby = linia.split()
        dane.append(liczby)
    return dane


def znajdz_system(liczby):
    systemy_litery = {'A': 11, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16, 'G': 17}
    for i in range(0,11):
        systemy_litery[str(i)] = i + 1
    lacznie = []
    for liczba in liczby:
        for znak in liczba:
            lacznie.append(ord(znak))
    maks_cyfra = max(lacznie)
    system = systemy_litery[chr(maks_cyfra)]
    return system


wystepowania = {}
dane = wczytaj_dane()
for trzy_liczby in dane:
    system = znajdz_system(trzy_liczby)
    # print(trzy_liczby, system)
    if system not in wystepowania:
        wystepowania[system] = 1
    else:
        wystepowania[system] += 1

print()

for system in sorted(wystepowania.keys()):
    print(f'System {system} - {wystepowania[system]} wystąpień')
