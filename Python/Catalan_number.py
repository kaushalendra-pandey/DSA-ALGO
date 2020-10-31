def catalan_number(n):
    dp = [0 for i in range(n+1)]

    dp[0],dp[1] = 1,1

    for i in range(2,len(dp)):
        cur = 0
        for j in range(0,i):
            cur += dp[j]*dp[i-j-1]
        dp[i] = cur

    return dp[-1]

catalan_number(5)