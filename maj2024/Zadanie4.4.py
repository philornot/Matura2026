with open('liczby.txt', 'r') as plik:
    linie = plik.readlines()
    pierwsze = linie[0].split()
    pierwsze = [int(liczba) for liczba in pierwsze]

srednia_max = 0
zapisana_dlugosc = 0
pierwszy_element = 0

for dlugosc in range(50, len(pierwsze) + 1):
    suma = sum(pierwsze[:dlugosc])
    srednia = suma / dlugosc

    if srednia > srednia_max:
        srednia_max = srednia
        zapisana_dlugosc = dlugosc
        pierwszy_element = pierwsze[0]

    for przesuniecie in range(dlugosc, len(pierwsze)):
        # Dodajemy ostatni element i usuwamy pierwszy
        suma = suma + pierwsze[przesuniecie] - pierwsze[przesuniecie - dlugosc]
        srednia = suma / dlugosc

        if srednia > srednia_max:
            srednia_max = srednia
            zapisana_dlugosc = dlugosc
            pierwszy_element = pierwsze[przesuniecie - dlugosc]

print(f"{srednia_max:.2f} {zapisana_dlugosc} {pierwszy_element}")