class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows < 1: return []
        result = []
        
        for i in range(1, numRows + 1):
            current = [0] * i
            current[0] = current[-1] = 1
        
            for j in range(1, i - 1):
                current[j] += result[i - 2][j - 1] + result[i - 2][j]

            result.append(current)
            
        return result
        
#         # Base case, assumed numRows >= 0
#         result = [[1], [1,1]]
#         if numRows < 3: return result[:numRows]

#         for i in range(3, numRows + 1): # Accomodate python's [x,y)
#           # Build the result using the previous row
#           previous = result[i - 2]

#           # Init for this row
#           current = [0] * i # number of elems is i
#           current[0] = current[-1] = 1 # the beginning and end is always 1

#           for j in range(1, i - 1):
#               # The sliding window is 2 anyways
#               current[j] = previous[j - 1] + previous[j]

#           result.append(current)

#       return result
