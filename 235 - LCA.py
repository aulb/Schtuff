def lowestCommonAncestor(root, p, q):
    # Assumed unique, value needs to be in between
    while root:
        if root.val > p.val and root.val > q.val:
            root = root.left
        elif root.val < p.val and root.val < q.val:
            root = root.right
        else:
            return root
    # Write recursive solution...
    # if root.val > p.val and root.val > q.val:
    # 	return lowestCommonAncestor(root.left, p, q)
    # elif root.val...
