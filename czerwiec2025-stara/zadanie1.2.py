def rozklad_na_czyn(liczba):
    czynniki = []
    dzielnik = 2
    while liczba > 1:
        if liczba % dzielnik == 0:
            czynniki.append(dzielnik)
            liczba = liczba // dzielnik
        else:
            dzielnik += 1
    return czynniki


def najmniejszy_czynnik_w_rozkl(liczba):
    rozkl = rozklad_na_czyn(liczba)
    min = 9999999999
    for i in rozkl:
        if i < min:
            min = i
    return min


def rozklad(n):
    P = {}
    for i in range(2, n + 1):
        P[i] = najmniejszy_czynnik_w_rozkl(i)
    for i in range(2, n + 1):
        if P[i] == i:
            P[i] = 1
        else:
            j1 = P[i]
            j2 = i / j1
            if j1 != j2 and P[j2] == 1:
                P[i] = 2
            else:
                P[i] = 3
    return P


while True:
    print("Dla 19:")
    print(rozklad(19), end='\n\n')
    liczba_input = int(input("Wprowadź liczbę: "))
    print(rozklad(liczba_input), end='\n\n')
