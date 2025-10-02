from wczytaj_dane import wczytaj_dane

w1, w2 = wczytaj_dane(przyklad=False)
w1 = sorted(w1)
w1 = w1[::-1]

print(w1[100])
odpowiedz2 = w1[100]