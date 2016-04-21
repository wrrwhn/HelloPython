from PIL import ImageGrab, Image
from os import popen
import clipboard as clip

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
	imgPath= 'd:/desk/'
	imageList= ['logo.png', 'python.gif', '547fdf5d61748.jpg']
	# imgPath= 'C:/Users/Yao/Desktop/'
	# imageList= ['Another.png', '006fl9Dwjw1f1txyi2j60g305o05onpd.gif', 'psb.jpg']
	return imgPath+ imageList[2]


def getFirstClipboardImage():
	path_str= 'd:/desk/screen_1.bmp'
	im= ImageGrab.grabclipboard()
	if isinstance(im, Image.Image):
		f= file(path_str, 'wb')
		im.save(f)
		f.close()
		return path_str
	else:
		return None

def getClipboardText():
	text= clip
	pass