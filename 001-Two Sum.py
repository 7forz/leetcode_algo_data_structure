class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # first check if appear twice
        if nums.count(target/2) == 2:  # Ω(n)
            result = []
            for i in range(len(nums)):
                if nums[i]==target/2:
                    result.append(i)
            return result
        else:
            nums_hash = {num:0 for num in nums}  # make a hash
            for i in range(len(nums)):
                if nums[i]==target/2:
                    continue
                elif (target-nums[i]) in nums_hash:  # O(1) for "in" operation for dict
                    return [i, nums.index(target-nums[i])]
