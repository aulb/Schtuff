class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or target is None:
            return False

        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1
        
        while low <= high:
            mid = (low + high) // 2
            # Mid // cols because cols * rows we wanna get cols
            # mid % cols to (0, cols - 1)
            num = matrix[mid // cols][mid % cols]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False
    
    
    # def binarySearch(self, row, target):
    #     low, high = 0, len(row) - 1
        
    #     while low <= high:
    #         middle = (low + high) // 2
    #         if row[middle] == target:
    #             return True
    #         elif row[middle] > target:
    #             high = middle - 1
    #         else:
    #             low = middle + 1
    
    #     return False
    
    # def searchMatrix(self, matrix, target):
    #     """
    #     :type matrix: List[List[int]]
    #     :type target: int
    #     :rtype: bool
    #     """
    #     if not matrix or matrix[0] or target is None: return False
        
    #     # Can we try binary searching the row
    #     m = len(matrix) - 1
    #     n = len(matrix[0]) - 1
        
    #     low, high = 0, m
        
    #     while low <= high:
    #         middle = (low + high) // 2
    #         if matrix[middle][0] <= target <= matrix[middle][n - 1]:
    #             return self.binarySearch(matrix[middle], target)
    #         elif matrix[middle][0] > target:
    #             # Check the first half
    #             high = middle - 1
    #         else:
    #             low = middle + 1
        
    #     return False
