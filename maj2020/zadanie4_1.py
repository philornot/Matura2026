def wczytaj_dane(przyklad=False):
    if przyklad:
        plik = 'Dane_PR2/przyklad.txt'
    else:
        plik = 'Dane_PR2/pary.txt'
    with open(plik) as f:
        linie = f.readlines()
    dane = []
    for linia in linie:
        dane.append(linia.split())
    return dane


def czy_pierwsza(liczba):
    if liczba in [0, 1, 4]:
        return False
    for i in range(2, liczba // 2):
        if liczba % i == 0:
            return False
    return True


# print(czy_pierwsza(4))

# print(wczytaj_dane(przyklad=True))

pary = wczytaj_dane(przyklad=False)
skladniki = []
for para in pary:
    liczba = int(para[0])
    if liczba < 4 or liczba % 2 != 0:
        continue
    # print(cyfra)
    pierwsze = []
    for i in range(liczba):
        if czy_pierwsza(i):
            pierwsze.append(i)

    znalezione = False

    for j in range(len(pierwsze)):
        if znalezione:
            continue
        for k in range(len(pierwsze)):
            if pierwsze[j] + pierwsze[k] == liczba:
                # print(f'{liczba}: {pierwsze[j]} + {pierwsze[k]}')
                skladniki.append([liczba, sorted([pierwsze[j], pierwsze[k]])])
                znalezione = True

for i in skladniki:
    l, s = i
    print(l, end=' ')
    for j in s:
        print(j, end=' ')
    print()
