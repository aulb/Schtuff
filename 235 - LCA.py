def lowestCommonAncestor(root, p, q):
    # Make sure p is the lower one
    p, q = p if p.val < q.val else q, q if p.val < q.val else p

    # Assumed unique, value needs to be in between
    while root:
        if root.val < p.val:
            # Go right
            root = root.right
        elif root.val > q.val:
            root = root.left
        else:
            return root
# TODO: Binary tree instead of BST
