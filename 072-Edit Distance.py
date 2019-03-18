class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)
       
        # 为了使初始化数据占一行和一列
        word1 = ' ' + word1
        word2 = ' ' + word2
        
        dp = [[None for _ in range(len2+1)] for _ in range(len1+1)]
        
        # init
        for i in range(len(word1)):
            dp[i][0] = i
        for j in range(len(word2)):
            dp[0][j] = j
        
        for m in range(1, len(word1)):
            for n in range(1, len(word2)):
                if word1[m] == word2[n]:
                    dp[m][n] = dp[m-1][n-1]  # 复制左上的
                else:
                    dp[m][n] = min(dp[m][n-1]+1, dp[m-1][n]+1, dp[m-1][n-1]+1)  # 加或删或改
        
        return dp[len1][len2]