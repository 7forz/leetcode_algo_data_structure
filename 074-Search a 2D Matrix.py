class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if (not matrix) or (not matrix[0]):
            return False
        
        # search from top-right corner
        _row = 0
        _col = len(matrix[0]) - 1
        
        while True:
            if target < matrix[_row][_col]:
                _col -= 1
                if _col < 0 or target > matrix[_row][_col]:
                    return False
            elif target > matrix[_row][_col]:
                _row += 1
                if _row == len(matrix):
                    return False
            else:
                return True