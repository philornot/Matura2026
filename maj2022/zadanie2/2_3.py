def algorytm(slowo):
    n = len(slowo)

    # print(f's={slowo}, n={n}')

    A = [0] * (n+1)
    # print(f'A: {A}')
    for i in range(1, n+1):
        litera = slowo[i-1]
        # print(i, litera, end=' ')
        if litera == 'a':
            A[i] = A[i-1] + 1
            # print(A, 'znaleziono a')
        else:
            A[i] = A[i-1]
            # print(A, 'NIE znaleziono a')

    B = [0] * (n+2)
    # print(f'\nB: {B}')
    for j in range(n, 1, -1):
        litera = slowo[j-1]
        # print(j, litera, end=' ')
        if litera == 'b':
            B[j] = B[j+1] + 1
            # print(B, 'znaleziono b')
        else:
            B[j] = B[j+1]
            # print(B, 'NIE znaleziono b')

    # print(f'\nA={A}\n'
    #      f'B={B}\n')
    k = 1
    for i in range(0, n+1):
        #print(f'i={i}',end=' ')
        #print(f'A[i]={A[i]}, B[i+1]={B[i+1]}')
        if A[i] + B[i+1] > k:
            k = A[i] + B[i+1]
    return k

# slowo = a300 b550 a300 b7 a280 b110
slowo = ''
for a in range(300):
    slowo += 'a'
for b in range(550):
    slowo += 'b'
for a in range(300):
    slowo += 'a'
for b in range(7):
    slowo += 'b'
for a in range(280):
    slowo += 'a'
for b in range(110):
    slowo += 'b'

# print(slowo)
print(algorytm(slowo)) # 990