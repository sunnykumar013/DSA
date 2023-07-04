class Solution:
    def countSubstrings(self, s: str) -> int:

        n = len(s)
        dp = [[False for i in range(n)] for j in range(n)]
        res = 0

        for i in range(n-1, -1, -1):

            dp[i][i] = True
            res +=1

            for j in range(i+1,n):
                if j - i == 1:
                    if s[i] == s[j]:
                        dp[i][j] = True

                    else:
                        dp[i][j] = False

                else:
                    if s[i] == s[j] and dp[i+1][j-1] ==True:
                        dp[i][j] = True

                    else:
                        dp[i][j] = False

                if dp[i][j] == True:
                    res +=1

        return res