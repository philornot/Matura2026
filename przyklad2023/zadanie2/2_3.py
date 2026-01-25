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


def testuj(A):
    for s in range(1, 201):
        if not rozgrywka(A, s):
            return False

    return True


A = []
x = 10
while not testuj(A):
    x += 1
    A = []
    for i in range(1, x, 1):
        A.append(i)

print(A)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# (x = 21)
