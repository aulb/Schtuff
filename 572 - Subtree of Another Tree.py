# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isMatch(self, s, t):
        # Both must be None
        if not (s and t):
            return t is s # Why not t is s, turns out doesn't matter LOL
        return s.val == t.val and self.isMatch(s.left, t.left) and self.isMatch(s.right, t.right)
    
    
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if self.isMatch(s, t): return True # Check immediately
        # If thats not the case, check left and right
        if not s: return False # t being None doesn't matter in this case, empty tree is always a subtree
        # Traverse the tree
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
