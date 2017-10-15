# This solution is for if there is any path that results in sum
# # Base case root is nothing but theres still sum to do
# if root == None:
#     return False

# # Otherwise
# remainder = sum - root.val
# if remainder == 0: return True
# elif remainder < 0: return False
# else:
#     return self.hasPathSum(root.left, remainder) or self.hasPathSum(root.right, remainder)


def hasPathSum(root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: bool
    """
    if root == None:
        return False
    
    # Base case root is nothing but theres still sum to do
    remainder = sum - root.val
    if root.left == None and root.right == None and remainder == 0:
        return True
    else:
        return hasPathSum(root.left, remainder) or hasPathSum(root.right, remainder)