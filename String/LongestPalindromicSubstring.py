class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        dp = [[False for i in range(n)] for j in range(n)]
        res = ""

        for i in range(n - 1, -1, -1):

            dp[i][i] = True
            res = s[i]
            # print(res)

            for j in range(i + 1, n):
                if j - i == 1:
                    if s[i] == s[j]:
                        dp[i][j] = True

                    else:
                        dp[i][j] = False

                else:
                    if s[i] == s[j] and dp[i + 1][j - 1] == True:
                        dp[i][j] = True

                    else:
                        dp[i][j] = False

        for i in range(n):
            for j in range(n):

                if dp[i][j] == True:
                    if (len(s[i:j + 1]) > len(res)):
                        res = s[i:j + 1]
                        print(res)

        return res