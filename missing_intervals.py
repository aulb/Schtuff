import sys

def get_missing_interval(intervals):
	intervals = sorted(intervals, key=lambda x: x[0])
	highest = -sys.maxsize
	n = len(intervals)
	result = []

	for i in range(n):
		highest = max(intervals[i][1], highest)
		if result and result[-1][1] < intervals[i][0] and highest <= intervals[i][1]:
			result.append((result[-1][1], intervals[i][0]))
		result.append(intervals[i])
	return result


if __name__ == '__main__':
	normal = [(0,1), (1,2), (3,5), (3,10), (11,12)]
	expected = [(0,1), (1,2), (2,3), (3,5), (3,10), (10,11), (11,12)]

	nonormal = [(0,1), (1,2), (3,5), (3,17), (11,12)]
	expected = [(0,1), (1,2), (2,3), (3,5), (3,17), (11,12)]
	
	print(get_missing_interval(nonormal))
