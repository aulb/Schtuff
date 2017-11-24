class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n: return 0
        # Generate all the perfect squares up to n
        squares = []
        counter = 1
        while counter ** 2 <= n: 
            squares.append(counter ** 2) 
            counter += 1
            
        lookup = list(map(lambda x: x + 1, range(n)))
        
        for square in squares:
            lookup[square - 1] = 1
            for index in range(n):
                if index - square < 0: continue
                lookup[index] = min(lookup[index], lookup[index - square] + 1)
        
        return lookup[-1]
