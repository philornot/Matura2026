from symulacja import symulacja, wczytaj_dane

odbiorcy = wczytaj_dane(przyklad=False)
n = len(odbiorcy)

komputery = {}
for i in range(1, n + 1):
    komputery[i] = [str(i)]

licznik = 0
komputery_po1 = symulacja(komputery, n, odbiorcy, liczba_rund=1)

for komputer, pakiety in komputery_po1.items():
    if not pakiety:
        licznik += 1

print(licznik)