with open('dane8.txt') as plik:
    dane = plik.read().split()

x = [int(liczba) for liczba in dane]
# x = [2,4,10,6,8,1,3,7,9,5]

n = len(x)
dp = [1]*n


for i in range(n):
    for j in range(0, i+1):
        if x[i] > x[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))