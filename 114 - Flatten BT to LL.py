# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):    
    def __init__(self):
        self.previous = None
    
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def _flatten(root):
            if not root: return
            _flatten(root.right)
            _flatten(root.left)
            root.left, root.right = None, self.previous
            self.previous = root
        _flatten(root)
