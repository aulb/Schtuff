Organizing first by input, organizing by topics?
- Watch Tushar's Video


# Graphs
- Detect a cycle in DAG


# String Manipulation



# Arrays
## Maximum Product SUBARRAY
Leetcode: 152
Link: http://www.geeksforgeeks.org/maximum-product-subarray/
Link: https://leetcode.com/problems/maximum-product-subarray/description/

Negative number, swap min and max

## Longest Increasing Subsequence
Leetcode: 300
Link: https://www.youtube.com/watch?v=CE2b_-XfVDk
Link: https://leetcode.com/problems/longest-increasing-subsequence/description/

LIS is of length one at every position
```
if arr[j] < arr[i]:
lookup[i] = max(lookup[j] + 1, lookup[i])
```

Pitfalls:
- Stacks won't work, can't greedily find minimum
Example: [1,3,6,7,9,4,10,5,6] - LIS: [1,3,6,7,9,10], found: [1,3,4,5,6]
- DP is not as trivial

# Binary Trees

# Binary Search Trees

# Integers

# Matrix

# Games

# Intervals
"""
Merging is by start time, easier to merge that way.
Runtime is affected mostly by the sorting operation O(nlogn).
"""
- Merge intervals (offline)
- Insert interval (online)
- Get rid of overlapping intervals (sort by start) : greedy, take as long as it doesn't overlap
- Largest set of non overlapping intervals (sort by end)


# Games
- Implement Maze
