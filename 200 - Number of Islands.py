class Solution(object):
    def modifyGrid(self, grid, i, j):
        # Infinitely recurse if we don't check
        if grid[i][j] == "0": return # Already zeroed out
        grid[i][j] = "0" 

        # walk four directions and zero out everything
        if not (i - 1 < 0): self.modifyGrid(grid, i - 1, j)
        if not (j - 1 < 0): self.modifyGrid(grid, i, j - 1)
        if not (i + 1 >= len(grid)): self.modifyGrid(grid, i + 1, j)
        if not (j + 1 >= len(grid[i])): self.modifyGrid(grid, i, j + 1)
        
        return 
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        num_island = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # Zero out the island
                if grid[i][j] == "1":
                    num_island += 1
                    self.modifyGrid(grid, i, j)
        return num_island
