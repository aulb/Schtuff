class Span:
    def __init__(self, left, right, height):
        self.left = left
        self.right = right
        self.height = height
        
        
class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]: return 0
        row, col = len(matrix), len(matrix[0])
        
        # No need to store a full 2d matrix lookup, just per row is enough
        left = [0 for _ in range(col)]
        right = [col for _ in range(col)]
        height = [0 for _ in range(col)]
        
        # final result
        max_area = 0
        for i in range(row):
            current_left, current_right = 0, col
            # calculate left and height
            for j in range(col):
                # Only do calculations if cell value is 1
                if matrix[i][j] == '1':
                    # update this row's left boundary values
                    left[j] = max(left[j], current_left)
                    
                    # height extended, meaning there is a '1' on the row above
                    height[j] += 1
                else:
                    # height of '0' is 0
                    height[j] = 0
                    
                    # reset
                    left[j] = 0 # boundary is the left edge
                    current_left = j + 1 # the next one
                
            # calculate right
            for j in range(col - 1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], current_right)
                else:
                    right[j] = col
                    current_right = j
                    
            # calculate area
            for j in range(col): max_area = max(max_area, (right[j] - left[j]) * height[j])
                
        return max_area
