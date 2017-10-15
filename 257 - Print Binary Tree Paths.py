# Do DFS? Trees and all, remember your DFS/BFS or traversals
# This is DFS cause pops, even if adjacents gets placed in first,
def binaryTreePaths(root):
    if not root:
        return []
    # initialize
    result, stack = [], [(root, "")]

    while stack:
        node, path = stack.pop()
        # At the leaves
        if not node.left and not node.right:
            result.append(path + str(node.val))

        # Check before putting in..., preorder trav
        if node.left:
            stack.append((node.right, path + str(node.val) + "->"))

        if node.right:
            stack.append((node.left, path + str(node.val) + "->"))
    return result
