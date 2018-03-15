class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        len_s = len(s)
        d = {}
        longest = temp_longest = 0
        i = 0

        while i<len_s:
            if s[i] in d:
                if temp_longest > longest:
                    longest = temp_longest
                i = d[s[i]] + 1  # 从上一次重复的地方的下一位再次开始
                temp_longest = 0  # clear
                d = {}  # clear
            else:
                d[s[i]] = i
                temp_longest += 1
                i += 1
        
        return max(longest, temp_longest)