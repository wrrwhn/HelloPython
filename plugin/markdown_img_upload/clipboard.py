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

def grabFileImage():
	# read from file
	imgPath= 'd:/desk/'
	imageList= ['logo.png', 'python.gif', '547fdf5d61748.jpg', '545C84178E97B9EDECB16C24A077DEB0.pptx']
	im= Image.open(imgPath+ imageList[2])
	return im