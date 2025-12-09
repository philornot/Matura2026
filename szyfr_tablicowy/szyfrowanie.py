def zapisz_w_tabeli(tekst, N):
    tabela = []
    for i in range(N):
        tabela.append([''] * N)

    i = 0
    for wier in range(N):
        for kol in range(N):
            if i > len(tekst):
                break
            tabela[wier][kol] = tekst[i]
            i += 1
    return tabela


def szyfr_z_tabeli(tabela):
    szyfr = ''
    N = len(tabela[0])

    for i in range(N):
        for j in range(N):
            szyfr = szyfr + tabela[j][i]
    return szyfr


def szyfruj(tekst, N):
    tabela = zapisz_w_tabeli(tekst, N)
    szyfr = ''
    N = len(tabela[0])
    licznik = 0
    for i in range(N):
        for j in range(N):
            szyfr = szyfr + tabela[j][i]
            licznik += 1
    while licznik < len(tekst):
        szyfr = szyfr + 'X'
        licznik += 1
    return szyfr


tekst = "LITWO OJCZYZNO MOJA TY JESTES JAK ZDROWIE - MICKIEWICZ"
N = 6

tabela_jawna = zapisz_w_tabeli(tekst, N)
print('Jawna tablica:')
for wiersz in tabela_jawna:
    print(wiersz)

print('\n======================\n')

szyfr = szyfr_z_tabeli(tabela_jawna)
print(f'Szyfr: {szyfr}')

print('\n======================\n')

tabela_zaszyfrowana = zapisz_w_tabeli(szyfr, N)
print('Zaszyfrowana tablica:')
for wiersz in tabela_zaszyfrowana:
    print(wiersz)

print('\n======================\n')

odszyfrowany_szyfr = szyfr_z_tabeli(tabela_zaszyfrowana)
print(f'Odczytany szyfr: {odszyfrowany_szyfr}')

print('\n======================\n')

print(f'Szyfr z dopełnieniem: {szyfruj(tekst, N)}')
