
# import 
import clipboard
import upload
import format
import utils

# method 
def uploadLocalFile():
	path= clipboard.getLocalImage()
	url= upload.upload(path)
	print format.format_markdown_img(url)

def uploadScreenShoot():
	tmp_path= clipboard.getClipboardImage()
	if tmp_path:
		qiniu_url= upload.upload(tmp_path, is_delete= True)
		print format.format_markdown_img(qiniu_url)
	else:
		print 'please shoot screen'

# run
uploadScreenShoot()


# uploadLocalFile()
# file_path= clipboard.getClipboardImage()

# # Screen Shot
# clipboard.saveScreenShoot(file_path='C:\Users\Yao\Desktop', file_extension='bmp')
# clipboard.saveScreenShoot()

# # time format 
# print utils.formatCurTime()