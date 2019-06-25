class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = {}
        
        for string in strs:  # e.g. 'abc'
            char_counts = [0] * 26  # a~z
            for char in string:
                char_counts[ord(char) - 97] += 1  # ord('a')=97
            char_counts = tuple(char_counts)  # make it hashable
            
            if char_counts in d:
                d[char_counts].append(string)
            else:
                d[char_counts] = [string]
        
        return list(d.values())