
class Person:
	# pass	# empty class
	
	# parameter
	count= 0

	# default method
	def __init__(self, name):
		self.name= name
		Person.count+= 1
	def __del__(self):
		Person.count-= 1

	# custom method
	def sayHello(self):
		print 'hello, %s / %d' % (self.name, Person.count) 		# diff namespace


# object init
p1= Person('Yao')
# print person with 
p1.sayHello()

p2= Person('luo')
p2.sayHello()
del p2

p1.sayHello()


