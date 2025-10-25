def wczytaj_odbiorcy(przyklad=False):
    if przyklad:
        plik = 'odbiorcy_przyklad.txt'
    else:
        plik = 'odbiorcy.txt'
    with open(plik, 'r') as f:
        linie = f.read()
    return linie.split()

def symulacja(komputery_startowe, n, odbiorcy, liczba_rund=None):
    if liczba_rund is None:
        liczba_rund = n

    komputery_aktualny_stan = komputery_startowe.copy()

    for runda in range(liczba_rund):
        komputery_nastepna_runda = {}
        for i in range(1, n + 1):
            komputery_nastepna_runda[i] = []

        for nadawca in range(1, n + 1):
            odbiorca_str = odbiorcy[nadawca - 1]
            odbiorca = int(odbiorca_str)

            pakiety_do_wyslania = komputery_aktualny_stan[nadawca]
            komputery_nastepna_runda[odbiorca].extend(pakiety_do_wyslania)

        komputery_aktualny_stan = komputery_nastepna_runda

    return komputery_aktualny_stan

def pelna_symulacja(komputery, n, odbiorcy):
    rundy = []
    for numer_rundy in range(1, n + 1):
        # print(f'Symulacja dla rundy {numer_rundy}')
        runda = symulacja(komputery, n, odbiorcy, liczba_rund=numer_rundy)
        rundy.append(runda)
    return rundy