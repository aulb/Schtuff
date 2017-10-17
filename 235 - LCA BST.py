# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p = p if p.val < q.val else p
        q = q if p.val < q.val else q
        
        # Assumed unique, value needs to be in between
        while root:
            # root.val > p.val assures parent property
            if root.val > q.val and root.val > p.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root
