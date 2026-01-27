def dec_na_bin(liczba_dec):
    liczba_bin = ''
    while liczba_dec > 0:
        liczba_bin = liczba_bin + str(liczba_dec % 2)
        liczba_dec = liczba_dec // 2
    return liczba_bin[::-1]


def dec_na_cokolwiek(liczba_dec, baza_systemu):
    if baza_systemu > 10:
        return 'sorki nie da rady :('
    liczba_wynikowa = ''
    while liczba_dec > 0:
        liczba_wynikowa = liczba_wynikowa + str(liczba_dec % baza_systemu)
        liczba_dec = liczba_dec // baza_systemu
    return liczba_wynikowa[::-1]


def bin_na_dec(liczba_bin):
    liczba_dec = 0
    for i, cyfra in enumerate(liczba_bin[::-1]):
        if cyfra == '0':
            continue
        liczba_dec = liczba_dec + int(cyfra) * 2 ** i
    return int(liczba_dec)


def cokolwiek_na_dec(liczba, baza_systemu):
    if baza_systemu > 10:
        return 'sorki nie da rady :('
    liczba_dec = 0
    for i, cyfra in enumerate(liczba[::-1]):
        if cyfra == '0':
            continue
        liczba_dec = liczba_dec + int(cyfra) * baza_systemu ** i
    return int(liczba_dec)


def dodaj(baza_systemu, *liczby):
    if baza_systemu > 10:
        return 'sorki nie da rady :('
    suma = 0
    for liczba in liczby:
        suma = suma + cokolwiek_na_dec(liczba, baza_systemu)
    return dec_na_cokolwiek(suma, baza_systemu)


print(dec_na_cokolwiek(37, 5))
print(cokolwiek_na_dec('100101', 2))
print(dodaj(5, '132', '21'))
