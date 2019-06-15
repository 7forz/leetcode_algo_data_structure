class Solution:
    def coinChange(self, coins, amount: int) -> int:
        
        # 最后一次决策：
        # 用了n个硬币 凑到了 amount-x 元
        # 若 x in coins，则 dp[amount]=n+1
        
        # 设dp[amount]为amount金额所需的硬币数，默认值为-1，初始值dp[0]=0
        # 转移条件：与最后一次决策相同
        # 最后返回dp[amount]
        
        dp = [-1] * (amount+1)
        dp[0] = 0
        
        # bottom-up
        for _amount in range(1, amount+1):
            candidates = []
            for coin in coins:
                offset = _amount - coin
                if offset >= 0 and dp[offset] != -1:  # if there is valid option
                    candidates.append(dp[offset])
            if candidates:
                dp[_amount] = min(candidates) + 1

        return dp[amount]