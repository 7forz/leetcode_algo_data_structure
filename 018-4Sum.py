import itertools

class Solution:
    def fourSum(self, nums:list, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        length = len(nums)
        results = set()
        d = {}
        for i in range(length):
            if nums[i] not in d:
                d[nums[i]] = [i]  # record position
            elif len(d[nums[i]]) < 4:  # 避免4个以上的重复
                d[nums[i]].append(i)

        for (i,j,k) in itertools.combinations(range(length-1), 3):
            to_find = target - nums[i] - nums[j] - nums[k]
            if to_find in d and max(d[to_find]) > k:
                sorted_tuple = tuple(sorted((nums[i],nums[j],nums[k],to_find)))
                results.add(sorted_tuple)  # 重复了也不影响

        return list(results)