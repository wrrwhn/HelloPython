
import sys




# method def
def read(fileName):
	'''read the file'''
	try:
		f = file(fileName)
		content= ''
		while True:
			line = f.readline()
			if 0 != len(line):
				content+= line
			else:
				break;
		print content
		f.close()
	except IOError:
		print 'read file failed'
	except Exception, e:
		print 'Exception: i cannot handle it'

# check
print sys.version, sys.version_info

# program
if len(sys.argv)< 2:
	print 'please input the args'
	sys.exit()

if sys.argv[1].startswith('--'):
	option= sys.argv[1][2:]
	if 'version'== option:
		print 'version= 0.9.0.8'
	else:
		print 'unknown option'
else:
	for fileName in sys.argv[1:]:
		read(fileName)

# windows
	# command
	# python internal_sys.py output.txt object.data null