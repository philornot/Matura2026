def wczytaj_dane(przyklad=False):
    if przyklad:
        plik = 'Dane_PR2/przyklad.txt'
    else:
        plik = 'Dane_PR2/pary.txt'
    with open(plik) as f:
        linie = f.readlines()
    dane = []
    for linia in linie:
        dane.append(linia.split())
    return dane


pary = wczytaj_dane(przyklad=False)

def czy_rozwazane(liczba, slowo):
    if liczba == len(slowo):
        return True
    return False

rozwazane = []
for i in range(len(pary)):
    liczba, slowo = int(pary[i][0]), pary[i][1]

    if czy_rozwazane(liczba, slowo):
        rozwazane.append((liczba, slowo))


#     liczba1, slowo1 = int(pary[i][0]), pary[i][1]
#     liczba2, slowo2 = int(pary[i + 1][0]), pary[i + 1][1]
# if liczba1 < liczba2 or (liczba1 == liczba2 and sorted(slowo2)[-1] < sorted(slowo2)[-1]):

for i, j in rozwazane:
    print(i, j)