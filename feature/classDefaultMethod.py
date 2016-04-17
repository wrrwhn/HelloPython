
class Object:
	def __init__(self, val):
		print 'init'
		self.val= val
	def __del__(self):
		print 'del'
	def __str__(self):
		return "['val': '%d']" % self.val
	def __lt__(self, other):
		if self.val< other.val:
			return 1
		elif self.val== other.val:
			return 0
		else:
			return -1
	def __getitem__(self, key):
		return self.val
	def __len__(self):
		return len(str(self.val))

obj= Object(10)
other= Object(9)

print str(obj), obj< other, obj[10], len(obj)
