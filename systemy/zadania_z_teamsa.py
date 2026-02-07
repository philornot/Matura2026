def dec_na_cokolwiek(liczba_dec, system):
    if liczba_dec == 0:
        return "0"
    liczba_wynik = ""
    while liczba_dec > 0:
        liczba_wynik = str(liczba_dec % system) + liczba_wynik
        liczba_dec = liczba_dec // system
    return liczba_wynik


def cokolwiek_na_dec(liczba, system):
    return int(str(liczba), int(system))


def porownaj(liczba1, system1, liczba2, system2):
    l1, l2 = f'{liczba1}_{system1}', f'{liczba2}_{system2}'
    liczba1 = cokolwiek_na_dec(liczba1, system1)
    liczba2 = cokolwiek_na_dec(liczba2, system2)
    if liczba1 > liczba2:
        return f"{l1} > {l2}"
    elif liczba1 < liczba2:
        return f"{l1} < {l2}"
    else:
        return f"{l1} = {l2}"


def dodaj(liczba1, system1, liczba2, system2):
    l1, l2 = f'{liczba1}_{system1}', f'{liczba2}_{system2}'
    liczba1 = cokolwiek_na_dec(liczba1, system1)
    liczba2 = cokolwiek_na_dec(liczba2, system2)
    return f"{l1} + {l2} = {liczba1 + liczba2}_10"

def odejmij(liczba1, system1, liczba2, system2):
    l1, l2 = f'{liczba1}_{system1}', f'{liczba2}_{system2}'
    liczba1 = cokolwiek_na_dec(liczba1, system1)
    liczba2 = cokolwiek_na_dec(liczba2, system2)
    return f"{l1} - {l2} = {liczba1 - liczba2}_10"


print(porownaj(2011, 3, 134, 6))
print(porownaj(134, 5, 134, 6))
print(porownaj(2222, 3, 1111, 6))
print()
print(dodaj(101112, 3, 121, 9))
print(odejmij(101112, 3, 121, 9))
