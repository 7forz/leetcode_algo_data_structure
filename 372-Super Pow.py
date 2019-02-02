class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        # first method
        # a^(10*m+b)=(a^b)*(a^10)^m
        # result = 1
        # a = a % 1337
        # for num in reversed(b):
        #     result = result * (a ** num) % 1337
        #     a = (a ** 10) % 1337
        # return result % 1337
    
        # second method 费马小定理
        # 1337 = 7 * 191  phi(1337) = 6 * 190 = 1140
        pow = int(str(b).replace('[','').replace(']','').replace(' ','').replace(',',''))
        if a % 1337 == 0:
            return 0
        else:  # a含有其中一个质数 或a与1337互质
            a = a % 1337
            return a ** (pow % 1140) % 1337
