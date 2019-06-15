class Solution:
    def triangleNumber(self, nums) -> int:
        # e.g.
        #    i j    k
        # 12345677899
        
        nums.sort()
        length = len(nums)
        
        total = 0
        for high in range(length-1, 1, -1):  # 2 <= high <= n-1
            mid = high - 1
            low = 0
            while low < mid:
                if nums[low] + nums[mid] > nums[high]:
                    total += (mid - low)
                    mid -= 1
                else:
                    low += 1
        
        return total
                