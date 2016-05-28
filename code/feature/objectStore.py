
import cPickle as p 	# rename

# init
fileName= "object.data"
objList= ['mouse', 'keyboard', 'phone']

# write
f = file(fileName, 'w')
p.dump(objList, f)		# write object to file
f.close()

# read
f = file(fileName)
print p.load(f)			# read object from file
