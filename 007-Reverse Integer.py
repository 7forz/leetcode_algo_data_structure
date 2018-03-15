class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        result_list = ['-']*len(s)
        
        if s[0] == '-':
            for i in range(1, len(s)):
                result_list[i] = s[-i]
        else:
            for i in range(len(s)):
                result_list[i] = s[-i-1]
        
        result = int(''.join(result_list))
        if -1<<31 <= result < 1<<31:
            return result
        else:
            return 0