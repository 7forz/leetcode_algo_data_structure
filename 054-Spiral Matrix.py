class Solution:
    def spiralOrder(self, matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]

        |-------col
        |
        |
       row
        """
        if not matrix:
            return []

        row_length = len(matrix)
        col_length = len(matrix[0])

        result = []
        
        cur_row = 0
        cur_col = 0
        cur_direction = 'r'  # initial
        col_inner_r = col_inner_l = row_inner_u = row_inner_d = 0  # no repeat

        while True:
            result.append(matrix[cur_row][cur_col])
            if cur_direction == 'r':
                if (cur_col+1) == (col_length-col_inner_r):
                    cur_direction = 'd'
                    cur_row += 1
                    col_inner_r += 1
                else:
                    cur_col += 1
            elif cur_direction == 'd':
                if (cur_row+1) == (row_length-row_inner_d):
                    cur_direction = 'l'
                    cur_col -= 1
                    row_inner_d += 1
                else:
                    cur_row += 1
            elif cur_direction == 'l':
                if cur_col == col_inner_l:
                    cur_direction = 'u'
                    cur_row -= 1
                    col_inner_l += 1
                else:
                    cur_col -= 1
            else:  # 'u'
                if (cur_row-1) == row_inner_u:
                    cur_direction = 'r'
                    cur_col += 1
                    row_inner_u += 1
                else:
                    cur_row -= 1
            
            if len(result) == row_length * col_length:
                return result
