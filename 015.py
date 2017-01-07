
    
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

if __name__ == '__main__':
    print twoSum([1,2,3,0], 3)
    