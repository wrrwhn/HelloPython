
# import sublime*
import sublime, sublime_plugin
# import system or core
# import user-code

# method
def mkFormatShootImage():
	import os
	import sys
	sys.path.append(r'D:\server\python\Python33\Lib\site-packages')
	sys.path.append(r'C:\Users\Yao\AppData\Roaming\Sublime Text 3\Packages\ImageUpload')
	sys.path.append(r'C:\Users\Yao\AppData\Roaming\Sublime Text 3\Packages\ImageUpload\utils')

	from ImageUpload.utils.clipboard import saveScreenShoot
	from ImageUpload.utils.format import format_markdown_img
	import ImageUpload.utils.upload as uploader
	# print("\t-->Error")

	tmp_path= saveScreenShoot()
	if tmp_path:
		qiniu_url= uploader.upload(tmp_path, is_delete= True)
		return format_markdown_img(qiniu_url)
	else:
		return 'None'

# class for sublime
class ShootImageUploadCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		formatUrl= mkFormatShootImage()
		sublime.set_clipboard(formatUrl)
		self.view.insert(edit, self.view.sel()[0].begin(), formatUrl)