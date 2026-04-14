def wczytaj_dane():
    sciezka = 'trzyliczby.txt'
    with open(sciezka, 'r') as plik:
        linie = plik.readlines()
    dane = []
    for linia in linie:
        liczby = linia.split()
        dane.append(liczby)
    return dane

dane = wczytaj_dane()

liczba_znakow_w_pliku = 0
for trzy_liczby in dane:
    for liczba in trzy_liczby:
        liczba_znakow_w_pliku += len(liczba)
# print(liczba_znakow_w_pliku)

wystepowanie_cyfr = {}
for trzy_liczby in dane:
    # print(trzy_liczby, system)
    for liczba in trzy_liczby:
        for cyfra in liczba:
            if cyfra not in wystepowanie_cyfr:
                wystepowanie_cyfr[cyfra] = 1
            else:
                wystepowanie_cyfr[cyfra] += 1

for cyfra in sorted(wystepowanie_cyfr.keys()):
    frekw = wystepowanie_cyfr[cyfra] / liczba_znakow_w_pliku
    print(f'Częstotliwość dla cyfry {cyfra}: {round((frekw*100),2)}%')
