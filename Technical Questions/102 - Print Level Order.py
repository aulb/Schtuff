def levelOrder(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    # Node queue holds all the nodes on the same level
    node_queue = [root] 
    # Result holds results for each level [[1],[2,3],[4]]
    result = []

    while node_queue:
        # Container for current level results
        level_result = []
        
        # Container for leaves for the next while iteration
        leaves = []

        # All the nodes here are on the same level
        for node in node_queue:
            # Check if node is not None
            if not node:
                continue
            
            # Get the node val
            level_result.append(node.val)
            
            # Get the possible leaves
            leaves.extend([node.left, node.right])
        
        # Append to master return    
        if level_result:
            result.append(level_result)
        
        # Refresh the queue
        node_queue = [leaf for leaf in leaves if leaf] # This gets rid of None
            
    return result
