def height(node):
    if not node: return 0
    return max(height(node.left), height(node.right)) + 1
