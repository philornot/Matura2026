with open('dane8.txt') as plik:
    dane = plik.read().split()

x = [int(liczba) for liczba in dane]
# x = [2,4,10,6,8,1,3,7,9,5]

maks_dlugosc_podciagu = 0
podciag = [x[0]]
for i in range(len(x)-1):
    if x[i] < x[i+1]:
        podciag.append(x[i+1])
    else:
        if len(podciag) > maks_dlugosc_podciagu:
            maks_dlugosc_podciagu = len(podciag)
        podciag = [x[i+1]]

print(maks_dlugosc_podciagu)