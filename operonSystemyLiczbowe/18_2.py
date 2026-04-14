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
    for i in range(1,11):
        systemy_litery[str(i)] = i + 1
    #print(systemy_litery)
    lacznie = []
    for liczba in liczby:
        for znak in liczba:
            lacznie.append(ord(znak))
    maks = max(lacznie)
    system = systemy_litery[chr(maks)]
    return system

dane = wczytaj_dane()
liczby_int = []
for trzy_liczby in dane:
    system = znajdz_system(trzy_liczby)
    # print(trzy_liczby, system)
    for liczba in trzy_liczby:
        liczby_int.append(int(liczba, system))

print(max(liczby_int), min(liczby_int))
