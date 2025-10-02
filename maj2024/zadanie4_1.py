from wczytaj_dane import wczytaj_dane

w1, w2 = wczytaj_dane(przyklad=False)
licznik = 0
for i in w1:
    for j in w2:
        if j % i == 0:
            licznik += 1
            break

print(licznik)
odpowiedz1 = licznik