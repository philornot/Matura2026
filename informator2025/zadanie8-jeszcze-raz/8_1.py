with open('dane8.txt') as plik:
    dane = plik.read().split()

x = [int(liczba) for liczba in dane]
# x = [2,4,10,6,8,1,3,7,9,5]

# print(dane)

luki = []
parzyste = nieparzyste = 0
for i in range(len(x) - 1):
    luka = abs(x[i] - x[i + 1])
    luki.append(luka)
    if luka % 2 == 0:
        parzyste += 1
    else:
        nieparzyste += 1

print(f'{parzyste} {nieparzyste}')