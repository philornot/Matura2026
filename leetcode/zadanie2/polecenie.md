# Zadanie 2

Dane są dwie posortowane tablice nums1 i nums2 o rozmiarach odpowiednio m i n. Zwróć medianę z tych dwóch posortowanych
tablic.

```python
def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
```

## Przykład 1:

Wejście: nums1 = [1,3], nums2 = [2]
Wyjście: 2.00000
Wyjaśnienie: scalona tablica = [1,2,3], a mediana to 2.

## Przykład 2:

Wejście: nums1 = [1,2], nums2 = [3,4]
Wyjście: 2.50000
Wyjaśnienie: scalona tablica = [1,2,3,4], a mediana to (2 + 3) / 2 = 2.5. 