from wczytaj_dane import wczytaj_dane

liczby = wczytaj_dane(przyklad=False)

potegi_trojki = []
potega = 1
while potega <= 100000:
    potegi_trojki.append(potega)
    potega = potega * 3

licznik_poteg = 0
for liczba in liczby:
    if liczba in potegi_trojki:
        licznik_poteg += 1

print(licznik_poteg)
odp4_1 = str(licznik_poteg)

with open('odp4-1.txt', 'w') as plik_wyjsciowy:
    plik_wyjsciowy.write(odp4_1)
