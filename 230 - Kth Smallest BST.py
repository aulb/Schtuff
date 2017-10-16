# TODO again
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def count(self, root):
		# if at the end
		if not root: return 0
		return self.count(root.left) + self.count(root.right) + right_count + 1

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # Count nodes to the left
        count = self.count(root.left, 0)

        while root:
	        # kth smallest element on the left side
	        if k < count:
	        	root = root.left
	        	k += 1
	        # kth smallest element on the right side
	        elif k > count:
	        	root = root.right
	        	k -= 1
	        # else this is it
	        else: 
	        	return root

	    return None
