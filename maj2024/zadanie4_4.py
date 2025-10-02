from wczytaj_dane import wczytaj_dane

w1, w2 = wczytaj_dane(przyklad=False)
maks_srednia = float('-inf')
maks_dlugosc = 0
maks_poczatek = 0

for start in range(len(w1)):
    suma = 0
    for dlugosc in range(50, len(w1) - start + 1):
        suma += w1[start + dlugosc - 1]
        srednia = suma / dlugosc
        if srednia > maks_srednia:
            maks_srednia = srednia
            maks_dlugosc = dlugosc
            maks_poczatek = start

print(f"{maks_srednia} {maks_dlugosc} {w1[maks_poczatek]}")
odpowiedz4 = f"{maks_srednia} {maks_dlugosc} {w1[maks_poczatek]}"

# dla przykładu wychodzi zła odpowiedź (3.905 200 2), ale nie wiem co jest źle