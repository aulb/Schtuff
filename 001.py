"""
From leetcode.com/problems/two-sum

Exactly one solution.

Trading space for speed, hash table is built for this.
"""

def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # Save space 
    # idx = []
    
    # Solve using hash tables, in python's case dictionary
    # Stores indices
    hash_helper = {}

    # O(n) solution
    for i in range(len(nums)):
        # match = target - nums[i]
        # try:
        #     # If the match is already there, return
        #     # right away
        #     # idx.append(hash_helper[match])
        #     # idx.append(i)
        #     return [hash_helper[match], i]
        # except KeyError:
        #     # Otherwise save number and index
        #     hash_helper[nums[i]] = i
        ## Can do this
        if (target - nums[i]) in hash_helper:
            return [hash_helper[target - nums[i]], i]
        else:
            hash_helper[nums[i]] = i

    # Return empty list if not found
    return None


if __name__ == '__main__':
    nums = [0,4,3,2,1,21]
    target = 21

    print two_sum(nums, target)
    print [0, 5]

