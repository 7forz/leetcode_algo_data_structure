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
    
    def generate(self, current:str, current_left, remain_left, remain_right):
        if not remain_right:  # remain_right == 0
            self.results.append(current)
        elif remain_left:
            self.generate(current+'(', current_left+1, remain_left-1, remain_right)
            if current_left:  # current_left > 0
                self.generate(current+')', current_left-1, remain_left, remain_right-1)
        else:  # remain_left==0 and remain_right > 0
            self.generate(current+')', current_left-1, remain_left, remain_right-1)
