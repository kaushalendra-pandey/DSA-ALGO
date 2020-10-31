def longest_substring(a):
    if len(a) == 1:
        return a
    dp = [[None for i in range(len(a))] for j in range(len(a))]
    max_count = 0
    start = 0
    end = 0

    for g in range(len(a)):
        i = 0
        j = i + g
        while j < len(a):

            if g == 0:
                dp[i][j] = True
                i += 1
                j += 1
                start = i
                end = j
                max_count = max(g, max_count)

            elif g == 1:
                if a[i] == a[j]:
                    dp[i][j] = True
                    start = i
                    end = j
                    max_count = max(g, max_count)
                i += 1
                j += 1
            else:
                if a[i] == a[j] and dp[i + 1][j - 1] == True:
                    dp[i][j] = True
                    start = i
                    end = j
                    max_count = max(g, max_count)
                i += 1
                j += 1

    return max_count + 1  # to return max_lenght


    # to return max_lenght string

    # if start == end:
    #     return a[0]
    #
    # ans = ''
    # for i in range(start,end+1):
    #     ans += a[i]
    # return ans




a = "ab"
print(longest_substring(a))