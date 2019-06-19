class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(nums) - 1
        i = 0
        
        while i <= r:
            if nums[i] == 0:
                # 保证l左边的都是0
                nums[i], nums[l]  = nums[l], nums[i]  # swap
                l += 1
            if nums[i] == 2:
                # 保证r右边的都是2
                nums[i], nums[r]  = nums[r], nums[i]  # swap
                r -= 1
                i -= 1
            i += 1