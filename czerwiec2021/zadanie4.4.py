def wczytaj_dane(przyklad=False):
    if przyklad:
        plik = 'przyklad.txt'
    else:
        plik = 'napisy.txt'
    with open(plik, 'r') as f:
        return f.read().split()


dane = wczytaj_dane(przyklad=False)

c = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
haslo = ''

for linia in dane:
    cyfry = ''
    wynikowe_cyfry = ''

    if haslo[-3:] == 'XXX':
        break

    for znak in linia:
        if znak in c:
            cyfry += znak
    if len(cyfry) > 0:
        if len(cyfry) % 2 == 0:  # pewnie dało się to zrobić bez rozbijania na dwa przypadki ale działa
            for i in range(len(cyfry)):
                if i % 2 == 0:
                    wynikowe_cyfry += cyfry[i]
                else:
                    wynikowe_cyfry += cyfry[i] + ' '
        else:
            for i in range(len(cyfry) - 1):
                if i % 2 == 0:
                    wynikowe_cyfry += cyfry[i]
                else:
                    wynikowe_cyfry += cyfry[i] + ' '

    # print(wynikowe_cyfry.split(' '))
    wynikowe_cyfry = wynikowe_cyfry[:-1].split(' ')  # (bo ostatnim elementem byłoby '')

    for i in range(len(wynikowe_cyfry)):
        liczba = wynikowe_cyfry[i]
        if liczba == '':
            continue
        liczba = int(liczba)
        if liczba < 65 or liczba > 90:
            continue
        wynikowe_cyfry[i] = chr(liczba)

    if wynikowe_cyfry[0] != '':
        for i in wynikowe_cyfry:
            haslo += str(i)

print(haslo)
