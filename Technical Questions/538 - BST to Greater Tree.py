# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def change_sum(self, root, add_by):
        if not root: return add_by
        right_value = self.change_sum(root.right, add_by)
        root.val += right_value
        # Need to return left value, because [1,0,4,-2,null,3]
        left_value = self.change_sum(root.left, root.val)
        return left_value 
        
        
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # Get the sum from all right
        if not root: return 
        self.change_sum(root, 0)
        return root
