class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x<0:
            return False

        _sum = 0
        x_original = int(x)

        while x>0:
            _sum = _sum * 10 + x % 10
            x = x // 10
        return _sum == x_original