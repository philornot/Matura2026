plik = open('cyfry.txt', 'r')
liczby = []
for liczba in plik:
    liczby.append(int(liczba.strip()))
plik.close()

# podpunkt a)
parzyste = []
for liczba in liczby:
    if not liczba % 2:
        parzyste.append(liczba)

wynik_a = f'a) {len(parzyste)}'
print(wynik_a)

# podpunkt b)
suma_min = 10000000001
liczba_z_suma_min = 0
suma_max = 0
liczba_z_suma_max = 0

for liczba in liczby:
    suma = 0
    for cyfra in str(liczba):
        suma += int(cyfra)

    if suma > suma_max:
        suma_max = suma
        liczba_z_suma_max = liczba

    if suma < suma_min:
        suma_min = suma
        liczba_z_suma_min = liczba

wynik_b = f'b) {liczba_z_suma_max} oraz {liczba_z_suma_min}'
print(wynik_b)

# podpunkt c)
rosnace = []
for liczba in liczby:
    liczba = str(liczba)
    rosnaca = False

    for i in range(len(liczba)):
        if i == 0:
            rosnaca = True
        elif int(liczba[i]) > int(liczba[i - 1]):
            rosnaca = True
        else:
            rosnaca = False
            break

    if rosnaca:
        rosnace.append(liczba)

wynik_c = 'c) ' + ' '.join(rosnace)
print(wynik_c)

zapis = open('wyniki4.txt', 'w')
zapis.write(f'{wynik_a}\n'
            f'{wynik_b}\n'
            f'{wynik_c}')
zapis.close()
