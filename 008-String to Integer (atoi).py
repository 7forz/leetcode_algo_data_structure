import re

class Solution:
    def myAtoi(self, string):
        """
        :type string: str
        :rtype: int
        """
        string = string.strip()
        pattern = re.compile('[+-]?\d+')

        try:
            result = int(pattern.match(string).group())
            if result > 2147483647:
                return 2147483647
            elif result < -2147483648:
                return -2147483648
            else:
                return result
        except (ValueError, AttributeError):
            return 0