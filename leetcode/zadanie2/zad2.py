def merge_tablic(tab1, tab2):
    wynik = []
    i = 0
    j = 0

    while i < len(tab1) and j < len(tab2):
        if tab1[i] <= tab2[j]:
            wynik.append(tab1[i])
            i += 1
        else:
            wynik.append(tab2[j])
            j += 1

    while i < len(tab1):
        wynik.append(tab1[i])
        i += 1

    while j < len(tab2):
        wynik.append(tab2[j])
        j += 1

    return wynik


def tab_parzysta(tab):
    if len(tab) % 2 == 0:
        return True
    else:
        return False


def findMedianSortedArrays(nums1, nums2):
    tablica = merge_tablic(nums1, nums2)

    if tab_parzysta(tablica):
        mediana = float((tablica[len(tablica) // 2] + tablica[len(tablica) // 2]) / 2)
    else:
        mediana = float(tablica[len(tablica) // 2])

    return mediana


tablica1 = [1, 3]
tablica2 = [2]
print(findMedianSortedArrays(tablica1, tablica2))
