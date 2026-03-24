def wczytaj_dane():
    with open('dane3.txt') as plik:
        dane_raw = plik.read().strip().split('\n')
    dane = []
    for d in dane_raw:
        d1, d2 = d.split()
        dane.append((int(d1), int(d2)))
    return dane


def czy_zawiera(przedzial1, przedzial2):
    # czy przedzial1 zawiera w sobie przedzial2
    a1, b1 = przedzial1
    a2, b2 = przedzial2
    return a1 <= a2 and b1 >= b2


def oblicz_dlugosc_przedzialu(a, b):
    return b - a + 1


def klucz(przedzial):
    a, b = przedzial
    return oblicz_dlugosc_przedzialu(a, b)


# przykładowy łańcuch z tych przedziałów: E, D, A, C
A = (-2, 4)
B = (-4, 3)
C = (-3, 6)
D = (0, 3)
E = (1, 1)
F = (7, 9)
# print('czy C zawiera w sobie A:', czy_zawiera(C, A))
# print('czy E zawiera w sobie D:', czy_zawiera(E, D))
# print('czy D zawiera w sobie E:', czy_zawiera(D, E))

dane = wczytaj_dane()
# dane = [A, B, C, D, E, F]
dane.sort(key=klucz)
n = len(dane)
lancuch = [dane[0]]

for i in range(n-1):
    nastepny_przedzial = dane[i+1]
    ostatni_z_lancucha = lancuch[-1]
    if czy_zawiera(nastepny_przedzial, ostatni_z_lancucha):
        lancuch.append(nastepny_przedzial)

print(len(lancuch))