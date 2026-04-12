def wczytaj_dane(przyklad=False, czy_inty=True):
    sciezka = 'przyklad.txt' if przyklad else 'liczby.txt'
    with open(sciezka, 'r') as plik:
        liczby_str = plik.read().split()
    if czy_inty:
        return [int(liczba) for liczba in liczby_str]
    else:
        return liczby_str


liczby = wczytaj_dane(przyklad=False, czy_inty=False)
licznik = 0
pierwsza = ''
for liczba in liczby:
    if liczba[-1] == liczba[0]:
        if licznik == 0:
            pierwsza = liczba
        licznik +=1
print(licznik, pierwsza)