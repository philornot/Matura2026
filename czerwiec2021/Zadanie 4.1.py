plik = open('napisy.txt')
licznik = 0
for linia in plik:
    linia = linia.strip()
    for cyfra in linia:
        if cyfra.isdigit():
            licznik += 1

print(f"Licznik : {licznik  }")
plik.close()