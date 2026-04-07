def wczytaj_wagony(przyklad=False):
    sciezka_do_pliku = 'Dane/przyklad_pociagi.txt' if przyklad else 'Dane/pociagi.txt'
    with open(sciezka_do_pliku, 'r') as plik:
        raw = plik.read().split('\n')

    wagony = []
    for wagon in raw:
        if len(wagon.split()) == 0:
            continue
        pociag, nosnosc = wagon.split()
        wagony.append(int(nosnosc))
    return wagony


def czy_pierwsza(liczba):
    for n in range(2, liczba // 2):
        if liczba % n == 0:
            return False
        n += 1
    return True


wagony = wczytaj_wagony(przyklad=False)
# print(wagony)
pierwszy_sklad = []
licznik = 0
for wagon in wagony:
    if czy_pierwsza(wagon):
        pierwszy_sklad.append(wagon)
    if wagon == 41:
        licznik += 1

print(f'Liczba wagonów: {len(pierwszy_sklad)}\n'
      f'Liczba wagonów o wadze 41 ton: {licznik}')