class Solution:
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix: return 0
        longest_path_length = 1
        row, col = len(matrix), len(matrix[0])
        lookup = [[None] * col for _ in range(row)]
        
        def dfs(x, y):
            # if not yet there, make
            if not lookup[x][y]: 
                lookup[x][y] = 1 + max(
                    dfs(x - 1, y) if x - 1 >= 0 and matrix[x][y] < matrix[x - 1][y] else 0,
                    dfs(x + 1, y) if x + 1 < row and matrix[x][y] < matrix[x + 1][y] else 0,
                    dfs(x, y - 1) if y - 1 >= 0 and matrix[x][y] < matrix[x][y - 1] else 0,
                    dfs(x, y + 1) if y + 1 < col and matrix[x][y] < matrix[x][y + 1] else 0)
            return lookup[x][y]            

        
        for i in range(row):
            for j in range(col):
                longest_path_length = max(dfs(i, j), longest_path_length)
                
        return longest_path_length
    

        
            
#     def dfs(self, matrix, i, j):
#         stack = [(i, j, 1)]
#         row, col = len(matrix), len(matrix[0])
#         path_length = 1
        
#         while stack:
#             x, y, intermediate_path_length = stack.pop()
#             path_length = max(path_length, intermediate_path_length)

#             if x - 1 >= 0 and matrix[x][y] < matrix[x - 1][y]: stack.append((x - 1, y, intermediate_path_length + 1))
#             if x + 1 < row and matrix[x][y] < matrix[x + 1][y]: stack.append((x + 1, y, intermediate_path_length + 1))
#             if y - 1 >= 0 and matrix[x][y] < matrix[x][y - 1]: stack.append((x, y - 1, intermediate_path_length + 1))
#             if y + 1 < col and matrix[x][y] < matrix[x][y + 1]: stack.append((x, y + 1, intermediate_path_length + 1))
                
#         return path_length
