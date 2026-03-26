# what ale jak to nie da się
with open('napisy.txt') as plik:
    napisy = plik.read().split()

napisy = sorted(napisy)
print('proszę bardzo, posortowane:')
for napis in napisy:
    print(napis)