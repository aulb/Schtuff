class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0
        rows, cols = len(grid), len(grid[0])
        
        perimeter = 0
        
        for i in range(rows):
            for j in range(cols):
                # If its not a zero
                if grid[i][j]: 
                    perimeter += 4
                
                    # Check the four boundaries now
                    # Check the row before
                    if i - 1 >= 0 and grid[i - 1][j]: perimeter -= 1
                    # Check the row after
                    if i + 1 < rows and grid[i + 1][j]: perimeter -= 1
                    # Check the col before
                    if j - 1 >= 0 and grid[i][j - 1]: perimeter -= 1
                    # Check the col after
                    if j + 1 < cols and grid[i][j + 1]: perimeter -= 1

        
        return perimeter
