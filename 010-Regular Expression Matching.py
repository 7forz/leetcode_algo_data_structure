class Solution:
    def isMatch(self, text:str, pattern:str) -> bool:
        """ recursion method """
        if text and not pattern:
            return False
        if not text:
            if not pattern:
                return True
            elif len(pattern)>=2 and pattern[1]=='*':  # '' 'a*b*' -> '' 'b*'
                return self.isMatch(text, pattern[2:])
            else:  # len(pattern)==1
                return False
        
        first_letter_match = (text[0] == pattern[0]) or (pattern[0] == '.')
        if len(pattern)>=2 and pattern[1]=='*':
            if first_letter_match:
                # 'aaab' 'a*b' -> 'aab' 'a*b', 'a' 'a*a' -> 'a' 'a'  考虑贪婪与非贪婪匹配
                return self.isMatch(text, pattern[2:]) or self.isMatch(text[1:], pattern)
            else:
                return self.isMatch(text, pattern[2:]) # 'b' 'a*b' -> 'b' 'b'
        
        if first_letter_match:
            return self.isMatch(text[1:], pattern[1:])
        else:
            return False