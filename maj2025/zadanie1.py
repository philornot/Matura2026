wywolania = 0


def przestaw(n):
    global wywolania
    wywolania += 1
    r = n % 100
    a = r // 10
    b = r % 10
    n = n // 100
    if n > 0:
        w = a + 10 * b + 100 * przestaw(n)
    else:
        if a > 0:
            w = a + 10 * b
        else:
            w = b
    return w


lista_n = [316498, 43657688, 154005710, 998877665544321, 12243523524345234525345431234, 242341]

for n in lista_n:
    print(f'n={n},  wynik={przestaw(n)},    wywołania={wywolania}')

    k = len(str(n))
    if k % 2 == 0:
        print(f'k/2 = {int(k/2)}', end='\n\n')
    else:
        print(f'(k + 1)/2 = {int((k + 1)/2)}', end='\n\n')

    wywolania = 0
