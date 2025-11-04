sciezka_do_pliku = 'dane4.txt'
with open(sciezka_do_pliku, 'r') as plik:
    dane4 = plik.read().split()
    # print(dane4)

test_tab1 = [5, 2, 7, 10]
test_tab2 = [4, 11, 4, 1, 4, 7, 11, 12, 13, 14, 7, 0, 3]

# ciag = test_tab1
# ciag = test_tab2
ciag = dane4

krotnosc = {}
maks_krotnosc = 0
maks_luka = []
for i in range(len(ciag) - 1):
    luka = abs(int(ciag[i]) - int(ciag[i + 1]))
    # print(f'Luka: |{ciag[i]} - {ciag[i+1]}| = {luka}')
    if not krotnosc.get(luka):
        krotnosc[luka] = 1
    else:
        krotnosc[luka] += 1

    if krotnosc[luka] > maks_krotnosc:
        maks_krotnosc = krotnosc[luka]
        maks_luka = [luka]
    elif krotnosc[luka] == maks_krotnosc:
        maks_krotnosc = krotnosc[luka]
        maks_luka.append(luka)

print(f'Największa krotność to {maks_krotnosc} dla luki {maks_luka}')
