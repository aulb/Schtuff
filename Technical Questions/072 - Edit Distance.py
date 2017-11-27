class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not (len(word1) and len(word2)): return len(word1) or len(word2)
        n, m = len(word1) + 1, len(word2) + 1
        lookup = [[0 for x in range(n)] for y in range(m)]
        
        for i in range(m): lookup[i][0] = i
        for j in range(n): lookup[0][j] = j
            
        for i in range(1, m):
            for j in range(1, n):
                lookup[i][j] = min(lookup[i - 1][j] + 1, lookup[i][j - 1] + 1, lookup[i - 1][j - 1] + (word1[j - 1] != word2[i - 1]))

        return lookup[i][j]
