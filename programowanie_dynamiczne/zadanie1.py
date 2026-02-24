def findMinCost(fieldCost):
    n = len(fieldCost)
    dp = [0] * n
    dp[0] = fieldCost[0]
    dp[1] = fieldCost[1]
    for i in range(2, n):
        dp[i] = fieldCost[i] + min(dp[i - 1], dp[i - 2])
    return dp[n - 1]


fieldCost = [20, 25, 15, 30, 50, 7]
# dp = [20,25,35,55]

print(findMinCost(fieldCost))
