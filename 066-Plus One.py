class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        position = len(digits)-1
        digits[position] += 1
        
        while True:
            if digits[position] != 10:
                return digits
            else:
                digits[position] = 0
                position -= 1
                if position >= 0:  # 前面还有进一位
                    digits[position] += 1
                else:  # 前面没有了 增加一个1
                    digits.insert(0, 1)