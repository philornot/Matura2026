from wczytaj_dane import wczytaj_dane

w1, w2 = wczytaj_dane(przyklad=False)

najwieksza_srednia = 0
dlugosc_fragmentu = 0
pierwszy_element = 0

for start in range(len(w1)):
    for dlugosc in range(50, len(w1) - start + 1):

        suma = 0
        for i in range(start, start + dlugosc):
            suma += w1[i]

        srednia = suma / dlugosc

        if srednia > najwieksza_srednia:
            najwieksza_srednia = srednia
            dlugosc_fragmentu = dlugosc
            pierwszy_element = w1[start]

print(f"{najwieksza_srednia} {dlugosc_fragmentu} {pierwszy_element}")
odpowiedz4 = f"{najwieksza_srednia} {dlugosc_fragmentu} {pierwszy_element}"
