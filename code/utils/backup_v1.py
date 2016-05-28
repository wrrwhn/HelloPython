
import os
import time

source = ['/usr/bakcup/python/source/image']
target_dir = '/usr/bakcup/python/target/'
target= target_dir+ time.strftime('%Y%m%d%H%M%S')+ '.zip'
cmd= "zip -qr '%s' %s" % (target, ' '.join(source))

# program run success -> 0
if 0== os.system(cmd):
	print 'source had backup to target[%s]'% target
else:
	print 'backup failed'
