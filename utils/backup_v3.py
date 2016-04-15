
import os
import time

source = ['/usr/bakcup/python/source/image', '/usr/bakcup/python/source/doc']
target_dir = '/usr/bakcup/python/target/'
target= target_dir+ time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

# create backup path
if not os.path.exists(target):
	os.mkdir(target)
	print 'create path[%s]' % target

# allow to custom file name
comment= raw_input('Enter a comment:')
if 0== len(comment):
	target+= os.sep+ now+ ".zip"
else:
	target+= os.sep+ now+ '_'+ comment.replace(' ', '_')+ '.zip'
cmd= "zip -qr '%s' %s" % (target, ' '.join(source))

# program run success -> 0
if 0== os.system(cmd):
	print 'source had backup to target[%s]'% target
else:
	print 'backup failed'
