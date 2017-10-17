# def lowestCommonAncestor(self, root, p, q):
#     stack = [root]
#     parent = {root: None}
#     while p not in parent or q not in parent:
#         node = stack.pop()
#         if node.left:
#             parent[node.left] = node
#             stack.append(node.left)
#         if node.right:
#             parent[node.right] = node
#             stack.append(node.right)
#     ancestors = set()
#     while p:
#         ancestors.add(p)
#         p = parent[p]
#     while q not in ancestors:
#         q = parent[q]
#     return q
# This trick stack.pop() appears quite a lot

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	# Bizzare solution, not mines
	def lowestCommonAncestor(self, root, p, q):
		# Recursion breaker is here
	    if root in (None, p, q): return root
	    # Makes (left, right)
	    left, right = (self.lowestCommonAncestor(kid, p, q)
	                   for kid in (root.left, root.right))
	    return root if left and right else left or right
