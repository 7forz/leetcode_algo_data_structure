class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']
              }
        
        results = []
        for digit in digits:
            results = self.combination(results, dic[digit])
        return results

    def combination(self, list1, list2):
        if not list1:
            return list2
    
        result = []
        for l1 in list1:
            for l2 in list2:
                result.append(l1 + l2)
        return result