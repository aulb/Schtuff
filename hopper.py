"""
My assumption is that headings should be sequential (unless going back to the previous heading).
This for example is not a valid input because it jumps from heading 2 to 5. 
It is completely valid to go back from a higher heading to a much lower heading.

invalid = [Heading(1, ""),
	 	   Heading(2, ""),
	 	   Heading(5, ""),
	 	   Heading(3, "")]
"""
# These classes are considered from the handout.
class Node(object):
    def __init__(self, heading, parent):
        self.heading = heading
        self.children = []

        # Parent to make the code cleaner, space taxing
        self.parent = parent


    def add_children(self, node):
    	self.children.append(node)

    # Define the string representation
    def __repr__(self):
		heading_str = self.heading.__repr__()
		list_str = 'List('

		child_amount = len(self.children)
		for i in range(child_amount):
			list_str = list_str + self.children[i].__repr__() 
			# If its not the last one, don't add comma
			if i is not child_amount - 1:
				list_str = list_str + ','

		list_str = list_str + ')'

		node_str = 'Node(' + heading_str + ', ' + list_str + ')'
		return node_str


class Heading(object):
	def __init__(self, weight, text):
		self.weight = weight
		self.text = text


	def __repr__(self):
		return 'Heading(' + str(self.weight) + ', ' + repr(str(self.text)) + ')'


def outline(headings):
	# Initialization, no parent
	previous = Heading(0, "")
	root_node = previous_node = Node(previous, None)

	for current in headings:
		# If the current weight is smaller or the same as the previous, 
		# that means we need to go back	and find the right parent.
		# The distance variable does that for us to correctly find the parent.

		# Calculate distance, this way if distance is negative that means its invalid
		distance = previous.weight - current.weight + 1

		# If the distance is lesser than 0 that means that we hit the 
		# invalid example. i.e heading 2 -> heading 6
		if distance < 0:
			raise Exception('The new heading\'s weight is not in order.')
		else:
			while distance is not 0:
				previous_node = previous_node.parent
				distance = distance - 1

		# Attach node to
		current_node = Node(current, previous_node)
		previous_node.add_children(current_node)

		previous = current
		previous_node = current_node

	return root_node


if __name__ == '__main__':
	# Valid examples
	example = [Heading(1, "All About Birds"),
  			   Heading(2, "Kinds of Birds"),
  		       Heading(3, "The Finch"),
  			   Heading(3, "The Swan"),
  			   Heading(1, "Habitats"),
  			   Heading(2, "Wetlands")]

	example2 = [Heading(1, "All About Getting Hired"),
  			    Heading(2, "Preface"),
  		        Heading(2, "What To Do"),
  			    Heading(3, "Who To Look For"),
  			    Heading(1, "All About Doing Well In Your Job"),
  			    Heading(1, "All About Fun Stuff")]

  	# Will throw an error
  	invalid = [Heading(1, ""),
	 	       Heading(2, ""),
	 	   	   Heading(5, ""),
	 	       Heading(3, "")]

  	root_node = outline(example)
  	# View the output
  	print root_node