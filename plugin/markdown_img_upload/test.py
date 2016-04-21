
# import 
import clipboard
import upload
import format

# method 
def uploadLocalFile():
	path= clipboard.getLocalImage()
	url= upload.upload(path)
	print format.format_markdown_img(url)


# run
# uploadLocalFile()