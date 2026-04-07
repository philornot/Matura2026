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
powtarzajaca_nosnosc = maks_wystapien = maks_nr_pociagu = 0
for nr_pociagu, wagony in pociagi.items():
    lokalny_maks_wystapien = lokalna_powtarzajaca_nosnosc = 0
    wystapienia = {}
    for nosnosc in wagony:
        if nosnosc not in wystapienia:
            wystapienia[nosnosc] = 1
        else:
            wystapienia[nosnosc] += 1

        if wystapienia[nosnosc] > lokalny_maks_wystapien:
            lokalny_maks_wystapien = wystapienia[nosnosc]
            lokalna_powtarzajaca_nosnosc = nosnosc

    if lokalny_maks_wystapien > maks_wystapien:
        maks_wystapien = lokalny_maks_wystapien
        powtarzajaca_nosnosc = lokalna_powtarzajaca_nosnosc
        maks_nr_pociagu = nr_pociagu

print(f'Numer pociągu: {maks_nr_pociagu}\n'
      f'Najczęściej powtarzający się wagon w tym pociągu o nośności: {powtarzajaca_nosnosc}\n'
      f'Liczba wagonów o tej samej nośności w tym pociągu: {maks_wystapien}')
