from symulacja import pelna_symulacja, wczytaj_odbiorcy

odbiorcy = wczytaj_odbiorcy(przyklad=False)
n = len(odbiorcy)

komputery = {}
for i in range(1, n + 1):
    komputery[i] = [str(i)]

rundy = pelna_symulacja(komputery, n, odbiorcy)
numer = 0
maks_dla_rundy = {}
for runda in rundy:
    maks_pakietow = 0
    numer += 1
    if numer not in [1, 2, 4, 8]:
        continue

    for komputer, pakiety in runda.items():
        if len(pakiety) > maks_pakietow:
            maks_pakietow = len(pakiety)

    maks_dla_rundy[numer] = maks_pakietow

odp4_4 = ''
for i in maks_dla_rundy.values():
    odp4_4 += str(i) + ' '

print(odp4_4)
with open('odp4_4.txt', 'w') as plik:
    plik.write(odp4_4)

