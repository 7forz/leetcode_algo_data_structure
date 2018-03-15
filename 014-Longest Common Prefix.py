class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        chars = []
        chars_of_first_word = [char for char in strs[0]]

        i = 0
        try:
            while True:
                for word in strs:
                    if word[i] != chars_of_first_word[i]:
                        return ''.join(chars)
                chars.append(word[i])
                i += 1
        finally:
            return ''.join(chars)