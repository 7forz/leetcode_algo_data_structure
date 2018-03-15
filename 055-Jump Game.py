class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        current = 0
        if current == len(nums)-1:
            return True

        while True:
            steps = nums[current]
            if steps <= 0:  # 在之前最好的选择中都只能到达0步 则必然失败
                return False
            candidates = []
            for i in range(current+steps, current, -1):
                if i >= len(nums)-1:
                    return True
                else:
                    candidates.append((i+nums[i], i))  # (position + steps at position, position)
            current = max(candidates)[1]