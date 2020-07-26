class Solution:
    def numDecodings(self, s: str) -> int:
        ORD_0 = ord('0')
        ORD_6 = ord('6')
        ORD_9 = ord('9')

        ways = 1
        addition = 0

        s = s.replace('10', 'x').replace('20', 'x')  # 0必须与前一位结合
        if '0' in s:  # 如果还有0，则为非法输入
            return 0

        i = 1
        while i < len(s):

            last_digit_is_single = ways - addition  # 只有最后一位没有被结合，才有可能增加ways

            if (s[i-1] == '1' and ORD_0 <= ord(s[i]) <= ORD_9) or \
                    (s[i-1] == '2' and ORD_0 <= ord(s[i]) <= ORD_6):
                addition = last_digit_is_single  # 记录增加了多少
                ways += addition
            else:
                addition = 0

            i += 1

        return ways
