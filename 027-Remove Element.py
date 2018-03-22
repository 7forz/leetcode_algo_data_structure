class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        i = j = 0
        while i < length:
            if nums[i] == val:
                while i < length and nums[i] == val:
                    i += 1
                if i == length:
                    break
                nums[j] = nums[i]
            else:
                nums[j] = nums[i]
                i += 1
                j += 1
        return j