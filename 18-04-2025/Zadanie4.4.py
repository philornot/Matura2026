# Zadanie 4.4 z matury 2024 czerwiec
plik = open('odbiorcy.txt', 'r')
odbiorcy = []
for linia in plik:
    odbiorcy.append(int(linia.strip()))

plik.close()

n = len(odbiorcy)

pakiety_na_komputerach = []
for i in range(n):
    pakiety_na_komputerach.append([i + 1])

maksymalne_pakiety = []
for numer_rundy in range(1, 9):
    nowy_rozklad = []
    for i in range(n):
        nowy_rozklad.append([])

    for i in range(n):
        odbiorca = odbiorcy[i] - 1
        for pakiet in pakiety_na_komputerach[i]:
            nowy_rozklad[odbiorca].append(pakiet)

    pakiety_na_komputerach = nowy_rozklad

    if numer_rundy in [1, 2, 4, 8]:
        maksymalna_liczba = 0
        for pakiety in pakiety_na_komputerach:
            if len(pakiety) > maksymalna_liczba:
                maksymalna_liczba = len(pakiety)

        maksymalne_pakiety.append(maksymalna_liczba)

zapis = open('wyniki4.txt', 'w')
print(*maksymalne_pakiety, file=zapis)
print(*maksymalne_pakiety)
zapis.close()
