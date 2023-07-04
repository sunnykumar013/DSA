def logcommonsub(s1):
    n = len(s1)
    dp =[[0 for i in range(n+1)] for j in range(n+1)]
    print(dp)
    str1=""
    for i in range(1,n+1):
        for j in range(i-1,n+1):
            if(s1[i-1] == s1[j-1] and i != j):
                dp[i][j] = 1 + dp[i-1][j-1]
                str1 =str1 + s1[i-1]

            else:
                dp[i][j]= max(dp[i-1][j], dp[i][j-1])
                # dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    # print(str1,end=" ")

    return dp[n][n]

print(logcommonsub("abcabcbb"))