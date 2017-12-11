class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        """
        Try to make this iterative to really learn.
        """
        if not board or not word: return False
        
        # DFS setup
        stack = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.exist_helper(board, word, i, j): return True
        
        return False
        
    def exist_helper(self, board, word, i, j):
        if board[i][j] == word[0]:
            # At the end of the word
            if not word[1:]: return True
            
            # mark as visited
            board[i][j] = '#'
            
            # walk four ways
            if i - 1 >= 0 and self.exist_helper(board, word[1:], i - 1, j): return True
            if i + 1 < len(board) and self.exist_helper(board, word[1:], i + 1, j): return True
            if j - 1 >= 0 and self.exist_helper(board, word[1:], i, j - 1): return True
            if j + 1 < len(board[0]) and self.exist_helper(board, word[1:], i, j + 1): return True

            # mark as unvisited after done
            board[i][j] = word[0]
            
            # nothing was found
            return False
            
        return False
