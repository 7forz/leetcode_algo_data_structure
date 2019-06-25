class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []

        self.results = []
        self.generate('(', 1, n-1, n)  # the first must be '('

        return self.results

    def generate(self, current:str, unclosed_left, remain_left, remain_right):
        # unclosed_left: how many unclosed left parenthesis exist
        if remain_right == 0:
            self.results.append(current)
        elif remain_left > 0:
            self.generate(current+'(', unclosed_left+1, remain_left-1, remain_right)
            if unclosed_left > 0:
                self.generate(current+')', unclosed_left-1, remain_left, remain_right-1)
        else:  # remain_left==0 and remain_right > 0
            self.generate(current+')', unclosed_left-1, remain_left, remain_right-1)
