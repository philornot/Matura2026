# A = [1, 3, 1]
# A = [2,2,2,2]

def algorytm(n, A):
    k = 0
    B = [0] * n
    for i in range(n):
        if A[i] in B:
            k += 1
        B[i] = A[i]
    return k

# n = len(A)
# print(algorytm(n,A))