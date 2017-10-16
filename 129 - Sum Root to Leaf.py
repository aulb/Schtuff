# Interesting...
# # bfs + queue
# def sumNumbers2(self, root):
#     if not root:
#         return 0
#     queue, res = collections.deque([(root, root.val)]), 0
#     while queue:
#         node, value = queue.popleft()
#         if node:
#             if not node.left and not node.right:
#                 res += value
#             if node.left:
#                 queue.append((node.left, value*10+node.left.val))
#             if node.right:
#                 queue.append((node.right, value*10+node.right.val))
#     return res

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        self.res = 0
        self.dfs(root, 0)
        return self.res

    def dfs(self, root, value):
        if root:
            self.dfs(root.left, value*10+root.val)
            self.dfs(root.right, value*10+root.val)
            if not root.left and not root.right:
                self.res += value*10 + root.val
