class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = None
        i = j = 0  # j is not-dup index

        while i < len(nums):
            if nums[i] != prev:
                prev = nums[i]
                nums[j] = nums[i]
                i += 1
                j += 1
            else:
                i += 1
        return j