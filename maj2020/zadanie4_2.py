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

pary = wczytaj_dane(przyklad=True)

dlugosc_max = 0
szukane = ''
for i, slowo in pary:
    taki_sam = slowo[0]
    for litera in slowo:
        if litera in taki_sam:
            taki_sam += litera
        else:
            taki_sam = litera
        dlugosc = len(taki_sam)
        if dlugosc > dlugosc_max:
            dlugosc_max = dlugosc
            szukane = taki_sam
    print(szukane, dlugosc_max)
