# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        lh = 0 if root.left is None else self.maxDepth(root.left)
        rh = 0 if root.right is None else self.maxDepth(root.right)
        return max(lh, rh) + 1
    
    