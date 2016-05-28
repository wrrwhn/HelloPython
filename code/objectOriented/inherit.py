
# Class definition
class Object:
	'''Basic class'''
	def __init__(self, name, age):
		self.name= name
		self.age= age
	def toString(self):
		print "['name': '%s', 'age': '%d']" % (self.name, self.age)

class Person(Object):
	'''Person class'''
	def __init__(self, name, age, sex):
		Object.__init__(self, name, age)
		self.sex= sex
	def toString(self):
		print "['name': '%s', 'age': '%d', 'sex': '%s']" % (self.name, self.age, self.sex)

class Commodity(Object):
	'''Commodity class'''
	def __init__(self, name, age, price):
		Object.__init__(self, name, age)
		self.price= price
	# def toString(self):
	# 	print "['name': '%s', 'age': '%d', 'price': '%d']" % (self.name, self.age, self.age)

# Class using
person= Person('Yao', 27, 'man')
commodity= Commodity('Kindle Paperwhite', 1, 958.00)

objList= [person, commodity]
for item in objList:
	item.toString()