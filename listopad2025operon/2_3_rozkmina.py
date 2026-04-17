"""
notka: rozumowanie niżej jest poprawne. ale.
ale nie jest to algorytm hornera tylko klasyczna definicja wielomianu
wiec działa, ale w poleceniu proszą nas o hornera.
"""


# W(x) = x^2 + 2x - 1
# W = [1, 2, -1] -> n = 2
# W(4) = (4**2)*1 + (4**1)*2 + (4**0)*(-1)
# W(4) = (4**n)*W[0] + (4**(n-1))*W[1] + (4**(n-2))*W[2]
# W(x) = (x**n)*W[0] + (x**(n-1))*W[1] + (x**(n-2))*W[2]

# for i in range(0, n):  czyli od 0 do n-1 (dla W: od zera do 1)
# A(x) = (x**n)*A[i] + ... (x**(n-1))*A[i+1] + (x**(n-2))*A[i+2]

# for i in range(n-1, 1, -1): czyli od n-1 do 0 (dla W: od 1 do zera)
# A(x) = (x**n)*A[n-i] + ... (x**(n-1))*A[n-i+1] + (x**(n-2))*A[n-i+2]

def oblicz_wielomian(n, a, A):
    """
    :param n: dodatnia liczba całkowita będąca stopniem wielomianu A
    :param a: liczba całkowita, dla której należy policzyć wartość wielomianu A(x)
    :param A: tablica liczb całkowitych – współczynników wielomianu A, A=[an,an-1,...,a1,a0]
    :return: wartość wielomianu A(a)
    """
    wynik = 0
    for i in range(0, n + 1):
        wynik += (a ** (n - i)) * A[i]
    return wynik


def horner(n, a, A):
    """
    :param n: dodatnia liczba całkowita będąca stopniem wielomianu A
    :param a: liczba całkowita, dla której należy policzyć wartość wielomianu A(x)
    :param A: tablica liczb całkowitych – współczynników wielomianu A, A=[an,an-1,...,a1,a0]
    :return: wartość wielomianu A(a)
    """
    wynik = A[0]
    for i in range(n - 1, -1, -1):
        wynik = wynik * a + A[n - i]
    return wynik


W = [1, 2, -1]
n = 2
print(horner(n, 2, W))
print(oblicz_wielomian(n, 2, W))
