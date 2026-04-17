def horner(n, a, A):
    wynik = A[0]
    for i in range(n - 1, -1, -1):
        wynik = wynik * a + A[n - i]
    return wynik


def czy_nalezy_do_fibo(liczba):
    if liczba < 0:
        return False
    if liczba in [0, 1]:
        return True
    fibo = [0, 1, 1]
    while fibo[-1] <= liczba:
        fibo.append(fibo[-2] + fibo[-1])

    # print(f'sprawdzam czy {liczba} jest w {fibo}')
    if liczba in fibo:
        return True
    else:
        return False


def wczytaj_dane(przyklad=False):
    sciezka_do_pliku = 'przyklad_wielomiany.txt' if przyklad else 'wielomiany.txt'
    wielomiany = []
    with open(sciezka_do_pliku, 'r') as plik:
        for wielomian in plik.readlines():
            wielomian = wielomian.strip('\n')
            wielomian = wielomian.split(' ')
            wielomian = [int(e) for e in wielomian]
            n = wielomian.pop(0)
            wielomiany.append((n, wielomian))

    return wielomiany


dane = wczytaj_dane(przyklad=False)
#print(dane)

for wielomian in dane:
    n = wielomian[0]
    wielomian = wielomian[1]
    wartosc2 = horner(n, 2, wielomian)
    if czy_nalezy_do_fibo(wartosc2):
        print(n, end=' ')
        for e in wielomian:
            print(e, end=' ')
        print()

# W = [5, 1, 1, 1, 1, 1, -28]  # 5x^6 + x^5 + x^4 + x^3 + x^2 + x -28
# A = [3, 1, 0, 0, 5]  # 3x^4 + x^3 + 5
# for wielomian in A, W:
#     n = len(wielomian) - 1
#     print(horner(n, 2, wielomian))
