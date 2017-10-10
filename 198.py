# Can't rob TWO ADJACENT HOUSES TWO IN A ROW.
def rob(nums):
	# Multiple assignments
    last, now = 0, 0
    # Instead of using temp variable, we can do this! (don't forget)
    for i in nums: last, now = now, max(last + i, now)
    return now

# # EXP
# last = 0
# now = max(0 + 5, 0) = 5

# last = 5
# now = max(0 + 2, 5) = 5

# last = 5
# now = max(5 + 8, 5) = 13

# last = 13
# now = max(5 + 9, 13) = 14
# [5,2,8,9]
#
