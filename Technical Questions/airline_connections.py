from collections import defaultdict
def create_flights_adjacency(flights):
	adjacency_dictionary = defaultdict(list)
	for start, end in flights: adjacency_dictionary[start].append(end)
	return adjacency_dictionary

def get_connections(flights, start, end):
	if not flights: return []

	adjacency_dictionary = create_flights_adjacency(flights)
	if not adjacency_dictionary[start]: return []

	path = [start]
	visited = defaultdict(bool)
	stack = adjacency_dictionary[start]

	while stack and path[-1] != end:
		path.append(stack.pop())
		stack.extend(adjacency_dictionary[path[-1]])



	return []




if __name__ == '__main__':
	flights = [('YYZ', 'YVR'), ('YUL', 'YVR'), ('YVR', 'YUL'), ('YUL', 'YYZ')]
