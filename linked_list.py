class LinkedList:
	def __init__(self, value, next = None):
		self.value = value
		self.next = next
	def __repr__(self):
		return 'LinkedList({}, {})'.format(self.value, repr(self.next))


def reverse(item, tail = None):
	next = item.next
	item.next = tail
	if next is None:
		return item
	else:
		return reverse(next, item)

def reverse_iter():
	pass

def detect_circular():
	pass

def reverse_middle():
	pass

def binary_tree_to_linked_list():
	pass
