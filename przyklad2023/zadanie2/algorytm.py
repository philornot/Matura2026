def tura(k, A, s, B):
    for i in range(s, A[k - 1] - 1, -1):
        if B[i - A[k - 1]] and not B[i]:
            B[i] = True

    return B


def rozgrywka(A, s):
    B = [True] + [False] * s
    n = len(A)
    for k in range(1, n + 1):
        B = tura(k, A, s, B)

    return B[s]


# Zadanie 2.1
print(rozgrywka([1, 2, 3], 5))
print(rozgrywka([1, 2, 5, 10], 14))
print(rozgrywka([13, 5, 5, 2, 7], 17))
print(rozgrywka([7, 6, 5, 4, 3, 2, 1], 25))
