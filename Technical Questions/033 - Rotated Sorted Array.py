# # "Binary search the pivot"
# def find_pivot(array, low, high):
# 	# Does not work for chunks 
# 	# If low becomes higher not found
# 	if (high < low): return -1
# 	if (high == low): return low

# 	mid = (low + high) // 2
# 	print(low, mid, high)
# 	# If at the boundary [4,5,1,2,3] if mid = 2 and high = 4, arr[m] is not > arr[m + 1]
# 	# check if 1 > 2: goal to find 5 > 1
# 	# mid < high so that mid + 1 is valid
# 	if (mid < high and array[mid] > array[mid + 1]): return mid
# 	# 5 > 1
# 	# mid > low so that mid - 1 is valid, return mid - 1
# 	if (mid > low and array[mid] < array[mid - 1]): return mid - 1
# 	# if the lower values are greater than the middle, find the pivot in the first half
# 	if (array[low] >= array[mid]): return find_pivot(array, low, mid - 1)
# 	# if the lower values are less than the mid, find the pivot in the second half
# 	return find_pivot(array, mid + 1, high)

# def rotated_binary_search(array, target):
# 	# find pivot index, pivot is the biggest number in this case
# 	pivot = find_pivot(array, 0, len(array) - 1)

# 	# pivot is not found, array is not rotated, do normal binary search
# 	if (pivot == -1): return binary_search(array, target)

# 	if (array[pivot] == target): return pivot
# 	# pivot found, if target is lesser than the first element, check the second half
# 	if (target < array[0]): return binary_search(array[pivot + 1:], target)
# 	# if target is more than the first element, check the first half
# 	return binary_search(array[:pivot + 1], target)

# def binary_search(sorted_array, target):
# 	low, high = 0, len(sorted_array) - 1
# 	while low <= high: # If just lower high is unreachable
# 		middle = (low + high) // 2
# 		if sorted_array[middle] < target:
# 			low = middle + 1
# 		elif sorted_array[middle] > target:
# 			high = middle - 1
# 		else:
# 			return middle
# 	return -1


# if __name__ == '__main__':
# 	sorted_array = [1,5,6,7,9,10,21,33,35,50]
# 	rotated_array1 = [4,5,1,2,3]
# 	rotated_array2 = [1,2,3,4,5,6,0]
# 	rotated_array3 = [1,3,5,6,78,100]
# 	array = [1,2,3,4,5]

# 	# assert binary_search(sorted_array, 4) == -1
# 	# assert binary_search(sorted_array, 5) == 1
# 	# assert binary_search(sorted_array, 50) == len(sorted_array) - 1
# 	# assert binary_search(sorted_array, 1) == 0

# 	# assert find_pivot(rotated_array1, 0, len(rotated_array1) - 1) == 1
# 	# assert find_pivot(rotated_array2, 0, len(rotated_array2) - 1) == 5
# 	# print(find_pivot(rotated_array3, 0, len(rotated_array3) - 1))
# 	print(find_pivot(rotated_array3, 0, len(rotated_array3) - 1))
# 	assert find_pivot(rotated_array3, 0, len(rotated_array3) - 1) == -1


# 	# print(rotated_binary_search(rotated_array1, 1))
# 	# assert rotated_binary_search(rotated_array1, 5) == 1
# 	# assert rotated_binary_search(rotated_array1, 4) == 0
# 	# assert rotated_binary_search(rotated_array1, 1) == 2
# 	# assert rotated_binary_search(rotated_array1, 3) == 4

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # [4,0]
        # [5,6,7,0,1,2,4], target = 1
        # [4,5,6,7,0,1,2]
        # Assumed no duplicates
        # Is nums[middle] > target
        # nums[middle] > nums[low]
        if not nums: return -1

        low, high = 0, len(nums) - 1
        # len == 1 => low = high = 0, nums[low] == target! 
        while low <= high:
            mid = (high + low) // 2 # low + (high - low) // 2
            if nums[mid] == target: return mid

            # Sorted on the right side
            if nums[high] >= nums[mid]:
                # Check if the target is on the right side
                # target > nums[mid], target is greater than midpoint 
                # target <= nums[high], target is between high or equal to high 
                if target > nums[mid] and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

            # Sorted on the left side
            elif nums[mid] >= nums[low]:
                # Check if target belong on the left side
                if nums[mid] > target and target >= nums[low]:
                    high = mid - 1
                else:
                    low = mid + 1



        # Not found
        return -1
