n = int(input())
k = int(input())

dp = [[0 for i in range(n)] for j in range(2)]
dp[0][1] = k
dp[1][1] = k*(k-1)

for i in range(2,n):
    dp[0][i] = dp[1][i-1]
    dp[1][i] = (dp[0][i-1]+dp[1][i-1]) * (k-1)

print(dp[0][n-1] + dp[1][n-1])