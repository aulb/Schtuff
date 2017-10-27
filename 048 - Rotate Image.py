def transpose(matrix):
	n = len(matrix)
	for i in range(n):
		for j in range(i + 1, n):
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

def flip_y(matrix):
	n = len(matrix)
	for i in range(n):
		for j in range(n // 2):
			matrix[i][j], matrix[i][~j] = matrix[i][~j], matrix[i][j]


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # transpose(matrix)
        # flip_y(matrix)
        n = len(matrix)
        
        for i in range((n + n % 2) // 2):
            for j in range(i, n + ~i):
                # matrix[i][j], matrix[~j][i], matrix[~i][~j], matrix[j][~i] = matrix[~j][i], matrix[~i][~j], matrix[j][~i], matrix[i][j]
                matrix[i][j], matrix[i][~j], matrix[~i][~j], matrix[~i][j] = matrix[i][~j], matrix[~i][~j], matrix[~i][j], matrix[i][j]
