# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ## Iterative solution DFS Inorder
        # result, stack = [], []
        # while True:
        #     while root:
        #         stack.append(root)
        #         root = root.left
        #     # root is None here
        #     # If stack is empty that means we are done
        #     if not stack: return result
        #     # Pop is O(1)
        #     node = stack.pop()
        #     # Guaranteed to be something because `while root`
        #     result.append(node.val)
        #     root = node.right
        
        ## BFS
        if not root: return []
        queue, result = deque(), {}
        queue.append((0, root))
        while queue:
            level, node = queue.popleft()
            # Initialize the []
            level_list = result.get(level, [])
            if not level_list:
                result[level] = level_list
            level_list.append(node.val)
            
            if node.left: queue.append((level + 1, node.left))
            if node.right: queue.append((level + 1, node.right))
        
        levels = list(result.keys()) # keys are ints
        final_result = [None] * len(levels)
        for level in levels:
            final_result[level] = result[level]
        
        return final_result
            
        ## Recursive solution with DFS        
        # result = []       
        # def dfsInorder(root):
        #     if root: 
        #         dfsInorder(root.left)
        #         result.append(root.val)
        #         dfsInorder(root.right)
        # dfsInorder(root)
        # return result
