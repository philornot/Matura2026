def zapisz_wynik():
    odpowiedzi = {}
    for i in range(1, 4):
        with open(f'odp4-{i}.txt', 'r') as plik:
            odpowiedzi[i] = plik.read()

    wyniki = (f'Zadanie 4.1: {odpowiedzi[1]}\n'
              f'Zadanie 4.2: {odpowiedzi[2]}\n'
              f'Zadanie 4.3: {odpowiedzi[3]}')

    with open('wyniki4.txt', 'w') as plik:
        plik.write(wyniki)


zapisz_wynik()