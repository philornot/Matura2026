def wczytaj_dane(przyklad=False):
    sciezka = 'liczby_przyklad.txt' if przyklad else 'liczby.txt'
    with open(sciezka, 'r') as plik:
        linie = plik.read().split('\n')
        if '' in linie:
            linie.remove('')
        dane = []
        for linia in linie:
            linia = linia.split()
            linia = [int(i) for i in linia]
            dane.append(linia)
        return dane


def wystepowanie(l, lista):
    if l not in lista:
        return 0
    wyst = {}
    for liczba in lista:
        if liczba not in wyst:
            wyst[liczba] = 1
        else:
            wyst[liczba] += 1
    return wyst[l]


def rozklad_na_czynniki(liczba):
    rozklad = []
    for n in range(2, (liczba // 2) + 1):
        while liczba % n == 0:
            rozklad.append(n)
            liczba = liczba // n
    return rozklad


dane = wczytaj_dane(przyklad=False)
# for linia in dane:
#     print(linia)

# print(rozklad_na_czynniki(33))

l1, l2 = dane[0], dane[1]
odpowiedz = []
for liczba2 in l2:
    rozklad = rozklad_na_czynniki(liczba2)
    wyst = {}
    for liczba in rozklad:
        if liczba not in wyst:
            wyst[liczba] = 1
        else:
            wyst[liczba] += 1
    print(rozklad, wyst)
    ok = False
    for l in wyst.keys():
        ile_potrzeba = wystepowanie(l, rozklad)
        print(f'w rozkładzie {liczba2} jest {ile_potrzeba} liczb {l}')
        ile_jest = wystepowanie(l, l1)
        print(f'a w pierwszej linijce jest {ile_jest} liczb {l}')
        if ile_potrzeba > ile_jest:
            ok = False
            print('czyli brakuje!\n')
            break
        else:
            ok = True
            print('ok\n')
    if ok:
        odpowiedz.append(liczba2)

for odp in odpowiedz:
    print(odp, end=' ')