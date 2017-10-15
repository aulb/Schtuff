def twoSum(nums, k):
    lookup = [] 
    # Return list
    retnums = []
    for i in range(len(nums)):
        if (k - nums[i]) in lookup:
            retnums.append([nums[i], k - nums[i]])
        else:
            lookup.append(nums[i])
    return retnums


#http://stackoverflow.com/questions/480214/how-do-you-remove-duplicates-from-a-list-in-whilst-preserving-order
def f7(seq):
    seen = set()
    seen_add = seen.add 
    return [x for x in seq if not (x in seen or seen_add(x))]


def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    length = len(nums)
    retnums = []
    counter = 1
    for i in range(length):
        result = twoSum(nums[i + 1:], nums[i] * -1)
        if result != []:
            for r in result:
                r.append(nums[i])
                retnums.append(sorted(r))
    seen = []
    for r in retnums:
        if r not in seen:
            seen.append(r)
    return seen


if __name__ == '__main__':
    print twoSum([1,2,3,0], 2)
    r =  threeSum([1,2,3,-1,-2,1,0])
