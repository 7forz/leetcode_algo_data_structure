class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        
        s = s.upper()
        i = 0
        j = len(s) - 1
        
        while i <= j:
            if not (48 <= ord(s[i]) <= 57 or 65 <= ord(s[i]) <= 90):
                i += 1
                continue
            if not (48 <= ord(s[j]) <= 57 or 65 <= ord(s[j]) <= 90):
                j -= 1
                continue
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True