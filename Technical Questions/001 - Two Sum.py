# #!/usr/bin/env python
# """
# Given a list of sorted integers, find two integers that sums to k.
# """

# def two_int_sum(array, target):
#     check = {}
#     for number in array:
#         if check.get(number, False): return [target - number, number]
#         check[target - number] = True

#     return []

# if __name__ == '__main__':
#     # [2, 7, 11, 15], target = 9,
#     array1 = [2,7,11,15]
#     array2 = [2,1,6,3]
#     print(two_int_sum(array2, 9))

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for index, num in enumerate(nums):
            if target - num in lookup: return [index, lookup[target - num]]
            lookup[num] = index
