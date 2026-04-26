def cyfry(n):
    licznik = 0
    b = 1
    c = 0
    while n > 0:
        a = n % 10
        n = n // 10
        if a & 2 == 0:
            c = c + (b * (a // 2))
        else:
            c = c + b
            licznik += 1
        b = b * 10
    return c, licznik

while True:
    n = int(input('n='))
    print(cyfry(n),'\n')