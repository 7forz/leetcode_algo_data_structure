class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        half = len(nums) / 2
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
            if d[num] >= half:
                return num