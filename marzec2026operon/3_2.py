def wczytaj_pociagi(przyklad=False):
    sciezka_do_pliku = 'Dane/przyklad_pociagi.txt' if przyklad else 'Dane/pociagi.txt'
    with open(sciezka_do_pliku, 'r') as plik:
        raw = plik.read().split('\n')

    wagony = []
    for wagon in raw:
        if len(wagon.split()) == 0:
            continue
        pociag, nosnosc = wagon.split()
        wagony.append([int(pociag), int(nosnosc)])

    pociagi = {}
    for wagon in wagony:
        pociag, nosnosc = wagon
        if pociag not in pociagi:
            pociagi[pociag] = [nosnosc]
        else:
            pociagi[pociag].append(nosnosc)

    return pociagi


pociagi = wczytaj_pociagi(przyklad=False)
maks_wagonow = nr_maks_pociagu = suma_wag_maks_pociagu = 0
for nr_pociagu, wagony in pociagi.items():
    if len(wagony) > maks_wagonow:
        maks_wagonow = len(wagony)
        nr_maks_pociagu = nr_pociagu
        suma_wag_maks_pociagu = sum(wagony)

print(f'Numer najdłuższego pociągu: {nr_maks_pociagu}\n'
      f'Długość najdłuższego pociągu: {maks_wagonow}\n'
      f'Suma wag wagonów najdłuższego pociągu: {suma_wag_maks_pociagu}')