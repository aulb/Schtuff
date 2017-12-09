class Solution:                
    def zeroOut(self, matrix, i, j):
        # Zero out all the rows
        for row in matrix:
            # Need to visit ALL the Nones, don't accidentally mark None as 0
            if row[j] is not None: row[j] = 0
        
        # Zero out all the columns
        for col in range(len(matrix[i])):
            if matrix[i][col] is not None: matrix[i][col] = 0
    
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]: return 
        row = len(matrix)
        col = len(matrix[0])
        
        # Mark all the zeroes with None
        for i in range(row):
            for j in range(col):
                if not matrix[i][j]: matrix[i][j] = None
        
        # Get rid of Nones 
        for i in range(row):
            for j in range(col):
                if matrix[i][j] is None: 
                    self.zeroOut(matrix, i, j)
                    # Make sure this is zeroed out too
                    matrix[i][j] = 0
