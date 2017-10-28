class ToyHash:
	"""
	Force strings.
	"""
	def __init__(self):
		self.used = 0
		self.internal_size = 8
		self.keys = [None] * self.internal_size
		self.values = [None] * self.internal_size

	def __str__(self):
		pass

	# Python "_" private convention
	# Use Python's complicated
	def _maybe_grow(self):
		load_factor = self.used / self.internal_size
		if load_factor > 2 / 3:
			# Time to resize
			pass
		# Otherwise do nothing

	def keys():
		pass

	def values():
		pass

	def _del(self):
		pass

	def __setitem__(self, key, item):
		pass

	def __getitem__(self, key):
		pass
