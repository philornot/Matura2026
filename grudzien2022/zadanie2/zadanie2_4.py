def wczytaj_pary():
    sciezka_do_pliku = '../Dane_2212/pary.txt'
    with open(sciezka_do_pliku) as plik:
        dane_raw = plik.read().split('\n')

    pary = []
    for para in dane_raw:
        if para.strip() == '':
            continue
        liczba1, liczba2 = para.split()
        pary.append((int(liczba1), int(liczba2)))

    return pary


pary = wczytaj_pary()
print(pary)

# i dalej nie mam pojęcia co zrobić :/
