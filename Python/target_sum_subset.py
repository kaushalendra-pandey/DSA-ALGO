target = int(input())
# n = int(input())

str_arr = input().split(' ')
arr = [int(num) for num in str_arr]

dp = [[False for i in range(target+1)] for j in range(len(arr)+1)]

for row in range(len(arr)+1):
    for col in range(target+1):
        if row == 0 and col == 0:
            dp[row][col] = True
        elif row == 0:
            dp[row][col] = False
        elif col == 0:
            dp[row][col] = True
        else:
            if dp[row-1][col]:
                dp[row][col] = True
            else:
                val = arr[row - 1]
                if col >= val:
                    if dp[row-1][col-val]:
                        dp[row][col] = True


print(dp[len(arr)][target])