
# create
def hello():
		print 'def method'
def printMax(a, b):
	if a>= b:
		return a
	else:
		return b
def change(x):
	global y
	print 'first=', x, y
	x= 'new value'
	y= 'new value'
	print 'change to', x, y
def defaultValue(x, y='wahaha', z= 'yi?'):
	print x, y, z

# hello()
print printMax(3,5)
# x=100; y= 100;change(x);print 'real=', x, y;
# defaultValue(100, 100);defaultValue(100);defaultValue('fuck', z= ",too")


# 