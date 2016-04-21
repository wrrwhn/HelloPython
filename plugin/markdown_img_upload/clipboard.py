from PIL import ImageGrab, Image

# # read from clipboard
# im = ImageGrab.grabclipboard()		# return image or fileName list

# if isinstance(im, Image.Image):
# 	print 'got one image'
# elif im:
# 	for filename in im:
# 		try:
# 			print filename
# 			im = Image.open(filename)
# 		except IOError:
# 			pass
# 		else:
# 			print 'got an image'
# else:
# 	print 'clipboard is empty'


def getLocalImage():
	'''grab clipboard[0] into the temp and return the temp file path'''
	# read from file
	# imgPath= 'd:/desk/'
	# imageList= ['logo.png', 'python.gif', '547fdf5d61748.jpg']
	imgPath= 'C:/Users/Yao/Desktop/'
	imageList= ['Another.png', '006fl9Dwjw1f1txyi2j60g305o05onpd.gif', 'psb.jpg']
	return imgPath+ imageList[2]


def getFirstClipboardImage():
	pass