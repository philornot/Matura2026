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

    return B


A = []
for i in range(0, 501, 5):
    A.append(i)

s = 500

B = []
for i in range(s + 1):
    B.append(i)

B = rozgrywka(A, s)

licznik = 0
for pole in B:
    if pole:
        licznik += 1

print(licznik)
