from symulacja import wczytaj_odbiorcy, pelna_symulacja

odbiorcy = wczytaj_odbiorcy(przyklad=False)
n = len(odbiorcy)

komputery = {}
for i in range(1, n + 1):
    komputery[i] = [str(i)]

rundy = pelna_symulacja(komputery, n, odbiorcy)

numer=0
min_numer=9876
szukany_pakiet = ''
licznik =0
for runda in rundy:
    numer += 1
    for komputer, pakiety in runda.items():
        if str(komputer) in pakiety:
            if numer < min_numer:
                min_numer = numer
                szukany_pakiet = str(komputer)
                break


print(f'{min_numer}, {szukany_pakiet}')
with open('odp4_3.txt', 'w') as plik:
    plik.write(f'{min_numer}, {szukany_pakiet}')
