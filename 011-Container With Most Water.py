class Solution:
    
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maximum_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            maximum_area = max(maximum_area, min(height[left], height[right])*(right-left))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return maximum_area