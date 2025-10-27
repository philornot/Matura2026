from wczytaj_dane import wczytaj_dane

liczby = wczytaj_dane(przyklad=False)

def silnia(liczba):
    wynik = 1
    i = 2
    while i <= liczba:
        wynik = wynik * i
        i += 1
    return wynik

odp4_2 = ''
for liczba in liczby:
    suma_silni_cyfr = 0
    for cyfra in str(liczba):
        suma_silni_cyfr+= silnia(int(cyfra))

    if suma_silni_cyfr == liczba:
        odp4_2 += str(liczba) + ' '

print(odp4_2)
with open('odp4-2.txt', 'w') as plik_wyjsciowy:
    plik_wyjsciowy.write(odp4_2)
