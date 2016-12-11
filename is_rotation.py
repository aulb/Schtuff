def is_rotation(s1, s2):
	# Transform s1 -> 's1s1'
	return s2 in (s1 + s1)

if __name__ == '__main__':
	print is_rotation("waterbottle", "bottlewater")
	print is_rotation("waterbottle", "tlewaterbot")
