# TODO again
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
	# Counting the whole damn thing
	# The counting method has constant space TODO
	def kthSmallest(self, root, k):
		"""	
	    :type root: TreeNode
	    :type k: int
	    :rtype: int
	    """
		# In order traversal would work...
		count = []
		self.helper(root, count)

		# Check valid k
		if k - 1 < len(count):
			return count[k - 1]
		# else... error handle	    	

	def helper(self, node, count): # inOrderDFS
		# Memory is n
		if not node: return

		self.helper(node.left, count)
		count.append(node.val) # or node
		self.helper(node.right, count)
