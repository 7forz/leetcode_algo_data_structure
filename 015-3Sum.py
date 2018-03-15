import itertools

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        location_dict = {}
        used_numbers_dict = {}

        # avoid too many repeations such as [0,0,0,0,0,0,0,0,0,0,0,0], decrease to [0,0,0]
        num_appear_times = {}
        nums_decreased = []
        for num in nums:
            try:
                num_appear_times[num] += 1  # later appear
                if num_appear_times[num] < 4:  # no more repeat than 4 times
                    nums_decreased.append(num)
            except KeyError:
                num_appear_times[num] = 1  # first appear
                nums_decreased.append(num)
        nums = nums_decreased

        for i in range(len(nums)):
            if nums[i] in location_dict:  # avoid collision
                location_dict[nums[i]].append(i)
            else:
                location_dict[nums[i]] = [i]
        
        for (i,j) in itertools.combinations(range(len(nums)), 2):
            number_to_find = -nums[i]-nums[j]
            if number_to_find in location_dict:
                for k in location_dict[number_to_find]:
                    if (k!=i and k!=j) and (tuple(sorted((nums[i], nums[j], nums[k]))) not in used_numbers_dict):
                        result.append([nums[i], nums[j], nums[k]])
                        used_numbers_dict[tuple(sorted((nums[i], nums[j], nums[k])))] = True
        return result