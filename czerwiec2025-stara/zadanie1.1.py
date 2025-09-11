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


def czy_iloczyn_dwoch_roznych_pierwszych(liczba):
    czynniki = rozklad_na_czyn(liczba)
    if len(czynniki) != 2:
        return "NIE"
    elif czynniki[0] == czynniki[1]:
        return "NIE"
    else:
        return "TAK"


while True:
    liczba_input = int(input("Wprowadź liczbę: "))
    print(liczba_input, rozklad_na_czyn(liczba_input), czy_iloczyn_dwoch_roznych_pierwszych(liczba_input))
