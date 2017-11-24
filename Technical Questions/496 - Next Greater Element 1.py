# To the right of the index in nums1
# What if nums1 > nums2 in length
def next_greater_elemet(nums1, nums2):
	pass

if __name__ == '__main__':
	d = {}
	st = []
	ans = []

	for x in [1,3,4,2]:
		while len(st) and st[-1] < x:
		    d[st.pop()] = x
		st.append(x)
	
	for x in [4,1,2]:
		ans.append(d.get(x, -1))
