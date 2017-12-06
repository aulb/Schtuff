TODO:
- Fill bucket
- median of stream
- merge intervals
- wildcard matching
- study permutations 46 :: recursive backtracking
- construct binary tree from inorder and preorder
- queue using stack
- graph traversal, keep track of visited nodes
- unique paths
- convert 123 to one two three
- rotate image
- three sum
- bipartite graph

Done:
- http://www.geeksforgeeks.org/print-k-sum-paths-binary-tree/
```
def pathSum(self, root, sum):
    vector, result = [], []
    if not root: return result
    self.printAllKSum(root, sum, vector, result)
    
    for r in result:
        print(r)
    
def printAllKSum(self, root, sum, vector, result):
    if not root: return
    
    vector.append(root.val)
    
    self.printAllKSum(root.left, sum, vector, result)
    self.printAllKSum(root.right, sum, vector, result)
    
    sum_so_far = 0
    for i in range(len(vector) - 1, -1, -1):
        sum_so_far += vector[i]
        
        if sum_so_far == sum:
            result.append(vector[i:])
    
    vector.pop()
```
- https://leetcode.com/problems/basic-calculator/description/
