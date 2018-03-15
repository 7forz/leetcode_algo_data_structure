class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        pos = {}
        for (i, num) in enumerate(numbers):
            pos[num] = i + 1
        for (i, num) in enumerate(numbers):
            if (target-num) in pos:
                return [i+1, pos[target-num]]