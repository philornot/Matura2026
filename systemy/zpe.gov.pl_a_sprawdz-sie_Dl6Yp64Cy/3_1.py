def wczytaj_dane():
    with open('Plik_tekstowy_dane_a.txt') as plik:
        return plik.read().split()


def bin_na_dec(liczba_bin):
    liczba_dec = 0
    n = len(liczba_bin)
    for i, cyfra in enumerate(liczba_bin[::-1]):
        if cyfra == '0':
            continue

        liczba_dec = liczba_dec + int(cyfra) * 2 ** i

    if liczba_bin[0] == '1':  # obsługa liczb ujemnych wg U2
        liczba_dec = liczba_dec - 2 ** n

    return int(liczba_dec)


def sprawdz_wynik(plik_z_odpowiedziami_z_zadania):
    with open(plik_z_odpowiedziami_z_zadania, encoding='utf-8') as plik:
        odpowiedzi = plik.read().split()
    with open('odpowiedzi_a.txt', encoding='utf-8') as plik:
        wyniki = plik.read().split()

    if odpowiedzi == wyniki:
        return True

    for i in range(len(odpowiedzi)):
        if odpowiedzi[i] != wyniki[i]:
            print(f'W linijce {i + 1} coś się nie zgadza. Powinno być "{odpowiedzi[i]}" a jest "{wyniki[i]}".')


liczby_binarne = wczytaj_dane()
liczby_dec = [bin_na_dec(liczba_bin) for liczba_bin in liczby_binarne]

for i in range(len(liczby_dec)):
    if not -60 < liczby_dec[i] < 60:
        liczby_dec[i] = 'BŁĘDNE DANE\n'
    else:
        liczby_dec[i] = str(liczby_dec[i]) + '\n'

with open('odpowiedzi_a.txt', 'w') as plik:
    plik.writelines(liczby_dec)

if sprawdz_wynik('odpowiedz_do_zadania_3-1.txt'):
    print('Poprawna odpowiedź!')
