from functools import reduce

def LIS(nums):
	longest = [1] * len(nums) # increasing sub up until i

	for i, num in enumerate(nums): # doesn't matter, starts from 0
		for j in range(0, i):
			prev = nums[j]
			if num > prev:
				longest[i] = max(longest[i], longest[j] + 1)

	return reduce(lambda x, y: max(x, y), longest)

if __name__ == '__main__':
	array = [19, 9, 2, 5, 3, 7, 101, 18]
	print(LIS(array))
