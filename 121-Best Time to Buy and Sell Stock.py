class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        max_profit = 0
        lowest_so_far = prices[0]
        
        for price in prices:
            lowest_so_far = min(lowest_so_far, price)
            max_profit = max(max_profit, price - lowest_so_far)
        
        return max_profit