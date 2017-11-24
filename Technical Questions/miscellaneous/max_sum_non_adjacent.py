def max_sum_non_adjacent(nums):
	if not nums: return None
	if len(nums) < 3: return max(nums)

	# Lookup to see the previous' max sum so far
	lookup_previous_max = [0] * len(nums)
	lookup_previous_max[0] = nums[0]
	lookup_previous_max[1] = max(lookup_previous_max[0], nums[1])

	# Fill lookup "table"
	for i in range(2, len(nums)):
		lookup_previous_max[i] = max(lookup_previous_max[i - 1], lookup_previous_max[i - 2] + nums[i])

	print(lookup_previous_max)
	return max(lookup_previous_max)


if __name__ == '__main__':
	test1 = [1,0,2,9,3]
	test2 = [3,2,0,0,9,10]

	print(max_sum_non_adjacent(test2))
	assert(max_sum_non_adjacent(test2) == 13)
