# use python.zipfile to compress

import os
import time
import zipfile

# method def
def compress(source, target, name):
	'''Compress 

	compress files in source to target.'''
	# backup path init
	if not os.path.exists(target):
		os.mkdir(target)
		print 'create path[%s]' % target
	target+= os.sep+ name+ ".zip"
	# files compress
	fos= zipfile.ZipFile(target, 'w')
	source= traversePath(source)
	for file in source:
		fos.write(file)
	fos.close()
	print 'compress files to %s' % target

def traversePath(source):
	'''Traverse 

	traverse all files in the paths'''
	# clone and clean origin list
	tmpSource= source[:]
	for i in source:
		del i
	# traverse path
	for path in tmpSource:
		if os.path.isfile(path):
			print path
			source.append(path)
		else:
			for dirpath, dirname, filenames in os.walk(path):
				print dirpath, dirname, filenames
				for filename in filenames:
					source.append(os.path.join(dirpath, filename))
	# return 
	print 'traverse path: ', source
	return source


# object init
# linux
# source = ['/usr/bakcup/python/source/image', '/usr/bakcup/python/source/doc']
# target_dir = '/usr/bakcup/python/target/'
# windows
source = ['E:/temp/test/source/img', 'E:/temp/test/source/doc']
target_dir = 'E:/temp/test/target/'
target= target_dir+ time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')


# files compress
# print compress.__doc__
compress(source, target, now)