
# import
from PIL import ImageGrab, Image

# method
def getLocalImage():
	'''grab clipboard[0] into the temp and return the temp file path'''
	# read from file
	imgPath= 'd:/desk/'
	imageList= ['logo.png', 'python.gif', '547fdf5d61748.jpg']
	# imgPath= 'C:/Users/Yao/Desktop/'
	# imageList= ['Another.png', '006fl9Dwjw1f1txyi2j60g305o05onpd.gif', 'psb.jpg']
	return imgPath+ imageList[2]

def saveScreenShoot(file_path=None, file_name=None, file_extension=None):
	'''save screen shot to settup/ default path'''
	# import
	from utils import formatCurTime
	from os import sep
	
	# path/ name/ extension setup
	if not file_path:
		file_path= ""
	elif not file_path.endswith(sep):
		file_path+= sep
	if not file_name:
		file_name= formatCurTime()
	if not file_extension:
		file_extension= 'jpg'
	file_path= str.format('{0}{1}.{2}', file_path, file_name, file_extension)
	print ('save screen shot to ', file_path)

	# save  
	im= ImageGrab.grab()
	if isinstance(im, Image.Image):
		im.save(file_path)
	else:
		print ('save screen shoot fail')

def getClipboardImage():
	'''return path of the shoot / list or none'''
	# image
	im= ImageGrab.grabclipboard()
	if isinstance(im, Image.Image):

		# tmp save
		from os import getenv, path
		import uuid
		from utils import mkdirIfNotExists
		tmp_path= getenv('APPDATA')+ path.sep+ "markdown_tmp_image"+ path.sep+ str(uuid.uuid1())+ ".png"
		if not mkdirIfNotExists(tmp_path):
			print ('save fail to %s' % tmp_path)
			return None

		# save & return path
		try:
			im.save(tmp_path)
			# print('save file to %s succeed' % tmp_path)
		except IOError:
			print ('clipboard/im.save fail to %s: %s' % (tmp_path, e))
			tmp_path= None
		finally:
			return tmp_path

	# image path list
	elif im:
		index= 0
		for fileName in im:
			try:
				print ('\tfilename= %s' % fileName)
				im= Image.oepn(fileName)
				index += 1
			except IOError:
				pass
			else:
				print ('ImageList[%d].size= %s' % (index-1, im.size))
	else:
		# print im
		return None


def getClipboardText():
	pass


