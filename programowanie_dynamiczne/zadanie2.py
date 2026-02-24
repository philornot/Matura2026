# złodzieje nie mogą okradać dwóch domów, które ze sobą sąsiadują
# tj. jeśli okradli dom `i` to nie mogą okraść domu `i+1` ani `i-1`

def findMaxSum(house_val):
    n = len(house_val)
    okradzione = [0] * n

    okradzione[0] = house_val[0]
    okradzione[1] = max(house_val[0], house_val[1])

    for i in range(2, n):
        okradzione[i] = max(okradzione[i - 1], okradzione[i - 2] + house_val[i])

    return okradzione[n - 1]


house_val = [4, 14, 18, 6, 2]
okradzione = findMaxSum(house_val)
print(okradzione)
