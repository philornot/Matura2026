def strzalka(punkt1, punkt2):
    print(f'{punkt1} -> {punkt2}')


def rysuj(x, N):
    """
    x — liczba z przedziału od [1, N]
    N — liczba różnych punktów (od 1 do N)
    """
    if 2 * x <= N:
        strzalka(x, 2 * x)
        rysuj(2 * x, N)
    if 2 * x + 1 <= N:
        strzalka(x, 2 * x + 1)
        rysuj(2 * x + 1, N)

# Zadanie 2.1
# rysuj(1, 10)


# Zadanie 2.2
# rysuj(x=1, N=20) -> 19; N-1

# Zadanie 2.3
# rysuj(1, 2) # 1 strzałka do 2
# rysuj(1, 3) # 1 strzałka do 3

# rysuj(1, 4) # 2 strzałki do 4
# rysuj(1, 5) # 2 strzałki do 5
# rysuj(1, 6) # 2 strzałki do 6
# rysuj(1, 7) # 2 strzałki do 7
# rysuj(1, 8)  # 2 strzałki do 8

# rysuj(1, 9)  # 3 strzałki do 9
# rysuj(1, 10)  # 3 strzałki do 10
# itd...

# zależność logarytmiczna, logarytm z podstawą 2, ale zaokrąglony w dół do liczby całkowitej
# dla N = 2047 trzeba przejść po log_2 (2047) strzałkach
# log_2 (2047) < log_2 (2048) = 11 => ZAOKR.W.DÓŁ[log_2 (2047)] = 10

# odpowiedź do zadania 2.3: 10
