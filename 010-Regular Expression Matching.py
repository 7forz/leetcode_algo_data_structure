class Solution:
    def isMatch(self, text:str, pattern:str):
        """ memo
            python3  ~ 60ms
        """
        memo = {}

        def dp(i, j):
            # if (i,j) in memo:
            #     print('used memo',i,j)  # so it's faster
            if (i,j) not in memo:
                _text = text[i:]
                _pattern = pattern[j:]
                result = None

                if _text:
                    if not _pattern:
                        result = False
                else:  # text == ''
                    if not _pattern:
                        result = True
                    elif len(_pattern)>=2 and _pattern[1]=='*':  # 'a*b*' -> b*'
                        result = dp(i, j+2)
                    else:  # len(pattern)==1
                        result = False

                if result is None:
                    first_letter_match = (_text[0] == _pattern[0]) or (_pattern[0] == '.')
                    if len(_pattern)>=2 and _pattern[1]=='*':
                        if first_letter_match:
                            # 'a' 'a*a' -> 'a' 'a' , 'aaab' 'a*b' -> 'aab' 'a*b'  考虑贪婪与非贪婪匹配
                            memo[(i,j)] = dp(i, j+2) or dp(i+1, j)
                            return memo[(i,j)]
                        else:
                            memo[(i,j)] = dp(i, j+2)  # 'b' 'a*b' -> 'b' 'b'
                            return memo[(i,j)]
                    
                    if first_letter_match:
                        result = dp(i+1, j+1)
                    else:
                        result = False
                memo[(i,j)] = result
            return memo[(i,j)]

        return dp(0,0)


        """ recursive method 
            python3  ~ 1400ms"""
        
        # if text:
        #     if not pattern:
        #         return False
        # else:  # text == ''
        #     if not pattern:
        #         return True
        #     elif len(pattern)>=2 and pattern[1]=='*':  # 'a*b*' -> b*'
        #         return self.isMatch(text, pattern[2:])
        #     else:  # len(pattern)==1
        #         return False
        
        # first_letter_match = (text[0] == pattern[0]) or (pattern[0] == '.')
        # if len(pattern)>=2 and pattern[1]=='*':
        #     if first_letter_match:
        #         # 'aaab' 'a*b' -> 'aab' 'a*b', 'a' 'a*a' -> 'a' 'a'  考虑贪婪与非贪婪匹配
        #         return self.isMatch(text, pattern[2:]) or self.isMatch(text[1:], pattern)
        #     else:
        #         return self.isMatch(text, pattern[2:]) # 'b' 'a*b' -> 'b' 'b'
        
        # if first_letter_match:
        #     return self.isMatch(text[1:], pattern[1:])
        # else:
        #     return False
        
# import time
# start = time.clock()
# print(Solution().isMatch("aaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbcccccccccccccccccccccaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbccccccccccccccccccabcdefgaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbcccccccccccccccccccccaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbccccccccccccccccccabcdefgaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbcccccccccccccccccccccaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbccccccccccccccccccabcdefgaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbcccccccccccccccccccccaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbccccccccccccccccccabcdefg", "a*b*c*a*b*c*abc*de*f*ga*b*c*a*b*c*abc*de*f*ga*b*c*a*b*c*abc*de*f*ga*b*c*a*b*c*abc*de*f*g"))
# end = time.clock()
# print('counted', end-start)

# python -m profile this_file.py