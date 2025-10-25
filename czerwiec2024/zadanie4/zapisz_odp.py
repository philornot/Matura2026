def zapisz_odp():
    plik_wynikowy = 'wyniki4.txt'

    with open('odp4_2.txt', 'r') as plik:
        odp4_2 = plik.read().strip()

    with open('odp4_3.txt', 'r') as plik:
        odp4_3 = plik.read().strip()

    with open('odp4_4.txt', 'r') as plik:
        odp4_4 = plik.read().strip()

    odpowiedz_koncowa = (
        f'Zadanie 4.2: {odp4_2}\n'
        f'Zadanie 4.3: {odp4_3}\n'
        f'Zadanie 4.4: {odp4_4}\n'
    )

    with open(plik_wynikowy, 'w') as f:
        f.write(odpowiedz_koncowa)


zapisz_odp()
