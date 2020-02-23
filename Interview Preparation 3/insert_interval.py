class Interval:
	def __init__(self, start, end):
		self.start = start
		self.end = end


def insert(intervals, new_interval):
	start, end = new_interval.start, new_interval.end
	left, right = [], []


	for interval in intervals:
		curr_start, curr_end = interval.start, interval.end

		# determine if it goes to L/R of the new/merged interval(s)
		if start > curr_end:
			left.append(interval)
		elif end < curr_start:
			right.append(interval)
		# merge cases
		else:
			start = min(start, curr_start)
			end = max(end, curr_end)

	return left + [Interval(start, end)] + right
