class Solution:
    def trap(self, height) -> int:
        n = len(height)
        if n < 3:
            return 0
        
        l_max, r_max = height.copy(), height.copy()
        
        for i in range(1, n):
            l_max[i] = max(l_max[i-1], l_max[i])
        
        for i in range(n-2, 0, -1):
            r_max[i] = max(r_max[i+1], r_max[i])

        total = 0
        for i in range(n):
            total += min(l_max[i], r_max[i]) - height[i]
        
        return total