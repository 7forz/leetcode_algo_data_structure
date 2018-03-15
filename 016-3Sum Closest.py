class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        nums.sort()
        result_sum = float('inf')

        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums)-1
            while j < k:
                _sum = nums[i]+nums[j]+nums[k]
                bias = _sum - target
                if bias == 0:
                    return _sum
                if abs(bias) < abs(result_sum-target):
                    result_sum = _sum
                elif bias > 0:
                    k -= 1
                elif bias < 0:
                    j += 1
        return result_sum