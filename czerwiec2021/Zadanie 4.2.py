plik = open('napisy.txt')
licznik = 0
tablica = []
for linia in plik:
    linia = linia.strip()
    tablica.append(linia)


print(tablica)
plik.close()
haslo = ""
pozycja = 0
for i in range(len(tablica)):
    slowo = tablica[i]
    if (i + 1) % 20 == 0:
        haslo = haslo + slowo[pozycja]
        pozycja += 1

print(haslo)
