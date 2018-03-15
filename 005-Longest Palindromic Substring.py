class Solution:
    
    longest = 1
    longest_str = ''

    def check_palindrome(self, s:str, first:int, last:int, longest:int):
        len_s = len(s)
        while first>=0 and last<len_s:
            if s[first]==s[last]:
                longest += 2
                if longest > self.longest:
                    self.longest = longest
                    self.longest_str = s[first:last+1]
                first -= 1
                last += 1
            else:
                break

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        if len(s)==1:
            return s
        
        if len(s)==2:
            if s[0]==s[1]:
                return s

        for i in range(1, len(s)-1):  # not the first or the last
            self.check_palindrome(s, i-1, i+1, 1)  # check pattern 'aba'
        
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                if self.longest < 2:
                    self.longest = 2
                    self.longest_str = s[i:i+2]
                try:
                    self.check_palindrome(s, i-1, i+2, 2)  # check pattern 'abba'
                except IndexError:
                    pass
                
        if self.longest_str:
            return self.longest_str
        else:
            return s[0]