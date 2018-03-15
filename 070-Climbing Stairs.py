class Solution:
    mem = {1:1, 2:2}
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        
        example:
        1 === 1
        2 === 1+1
              2
        3 === 1+1+1
              1+2
              2+1
        4 === 1+1+1+1
              1+2+1
              2+1+1
              1+1+2
              2+2
        """
        if n in self.mem:
            return self.mem[n]
        else:
            self.mem[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return self.mem[n]