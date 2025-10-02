from wczytaj_dane import wczytaj_dane


def rozklad_na_czynniki(liczba):
    czynniki = []
    dzielnik = 2

    while liczba > 1:
        if liczba % dzielnik == 0:
            czynniki.append(dzielnik)
            liczba = liczba // dzielnik
        else:
            dzielnik = dzielnik + 1

    return czynniki


def policz_wystapienia(lista):
    slownik = {}
    for el in lista:
        if el in slownik:
            slownik[el] += 1
        else:
            slownik[el] = 1
    return slownik


w1, w2 = wczytaj_dane(przyklad=False)
w1_counter = policz_wystapienia(w1)
iloczyny = []

for l2 in w2:
    rozklad = rozklad_na_czynniki(l2)
    rozklad_counter = policz_wystapienia(rozklad)
    ok = True
    for k in rozklad_counter:
        if k not in w1_counter or rozklad_counter[k] > w1_counter[k]:
            ok = False
            break
    if ok:
        iloczyny.append(l2)

print(iloczyny)
odpowiedz3 = iloczyny
