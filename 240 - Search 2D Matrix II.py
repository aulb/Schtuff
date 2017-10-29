class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]: return False
        
        # n + m scan
        rows, cols = 0, len(matrix[0]) - 1
        while rows < len(matrix) and cols >= 0:
            if matrix[rows][cols] == target: return True
            elif matrix[rows][cols] < target: rows += 1
            elif matrix[rows][cols] > target: cols -= 1
        
        return False
