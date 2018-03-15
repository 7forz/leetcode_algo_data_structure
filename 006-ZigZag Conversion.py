class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows > len(s):
            return s
        
        results = []
        for _ in range(numRows):
            results.append([])

        row = 0
        direction = 1
        for char in s:
            results[row].append(char)
            if row+1 == numRows:  # e.g. for numRows=3, max(row)=2
                direction = -1
            elif row == 0:
                direction = 1
            row += direction
        
        result_str = ''
        for result in results:
            result_str += ''.join(result)
        return result_str