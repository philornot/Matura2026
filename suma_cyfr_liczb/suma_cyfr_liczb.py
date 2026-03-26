def wczytaj_dane():
    with open('dane.txt') as plik:
        return plik.read().split()


dane = wczytaj_dane()
print(dane)

liczby_i_sumy = {}
maks_suma = 0

for liczba in dane:
    suma = sum(int(cyfra) for cyfra in liczba)
    print(liczba, suma)
    liczby_i_sumy[suma] = liczba
    if suma > maks_suma:
        maks_suma = suma

print(f'Największa znaleziona suma to {maks_suma} dla liczby {liczby_i_sumy[maks_suma]}')
