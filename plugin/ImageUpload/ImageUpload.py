
# import sublime*
import sublime, sublime_plugin
# import system or core
# import user-code

# # import thread
# import threading


# method
def mkFormatImage(path):
	import sys
	sys.path.append(r'D:\server\python\Python33\Lib\site-packages')
	sys.path.append(r'C:\Users\Administrator\AppData\Roaming\Sublime Text 3\Packages\ImageUpload')
	sys.path.append(r'C:\Users\Administrator\AppData\Roaming\Sublime Text 3\Packages\ImageUpload\utils')

	from ImageUpload.utils.commonUtils import checkImage	
	import ImageUpload.utils.upload as uploader
	path= checkImage(path)
	qiniu_url= 'None'

	if not path:
		from ImageUpload.utils.clipboard import getClipboardImage
		path= getClipboardImage()

	if path:
		qiniu_url= uploader.upload(path, is_delete= True)

	return qiniu_url

# # class
# class MkUploadThread(threading.Thread):
# 	'''upload for markdown format in a thread'''
# 	def __init__(self, text, edit):
# 		self.text= text
# 		self.edit= edit
# 		threading.Thread.__init__(self)

# 	def run(self):
# 		path= sublime.get_clipboard()
# 		print(path)
# 		formatUrl= mkFormatImage(path)
# 		sublime.set_clipboard(formatUrl)
# 		if formatUrl:
# 			from ImageUpload.utils.format import format_markdown_img
# 			formatUrl= format_markdown_img(formatUrl)
# 			return formatUrl
# 		else:
# 			return None
# 		# mkUploadThread= MkUploadThread(self, edit)
# 		# mkUploadThread.start()


# class for sublime
class ScreenShotUploadMarkdownCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		path= sublime.get_clipboard()
		formatUrl= mkFormatImage(path)
		sublime.set_clipboard(formatUrl)
		if formatUrl:
			from ImageUpload.utils.format import format_markdown_img
			formatUrl= format_markdown_img(formatUrl)
		self.view.insert(edit, self.view.sel()[0].begin(), formatUrl)
