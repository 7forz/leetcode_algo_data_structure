class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        #  i    j
        #  axyzxa
        
        # dp[i][j] := s[i:j] 上回文序列的长度
        # initialize dp[i][i] = 1
        
        length = len(s)
        if s == s[::-1]:
            return length

        dp = [[0 for _ in range(length)] for _ in range(length)]
        for i in range(length):
            dp[i][i] = 1
        
        for j in range(1, length):
            for i in range(j-1, -1, -1):  # 0 <= i <= j-1
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2  # i增加 j减小，与for循环的方向相反（取的都是已有的值）
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j-1])
        
        return dp[0][length-1]