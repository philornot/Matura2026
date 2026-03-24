with open('dane8.txt') as plik:
    dane = plik.read().split()

x = [int(liczba) for liczba in dane]
# x = [2,4,10,6,8,1,3,7,9,5]

licznik = 0
for i in range(len(x)):
    for j in range(i, len(x)):
        if x[i] > x[j]:
            licznik += 1

print(licznik)
