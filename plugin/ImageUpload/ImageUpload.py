
# import sublime*
import sublime, sublime_plugin
# import system or core
# import user-code

# method
def mkFormatShootImage():
	import os
	import sys
	# sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

	from ImageUpload.utils.clipboard import saveScreenShoot
	from ImageUpload.utils.format import format_markdown_img
	import ImageUpload.utils.upload as uploader

	tmp_path= saveScreenShoot()
	if tmp_path:
		qiniu_url= uploader.upload(tmp_path, is_delete= True)
		return format_markdown_img(qiniu_url)
	else:
		return 'None'

# class for sublime
class ShootImageUploadCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, self.view.sel()[0].begin(), mkFormatShootImage())