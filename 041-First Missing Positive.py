class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)
        for u in range(length):
            correct_pos = nums[u]-1  # correct means [1,2,3,4, ..., n-1]
            while 1 <= nums[u] <= length and nums[u] != nums[correct_pos]:
                nums[u], nums[correct_pos] = nums[correct_pos], nums[u]
                correct_pos = nums[u]-1
        
        for u in range(length):
            if u+1 != nums[u]:
                return u+1
        
        return length + 1
