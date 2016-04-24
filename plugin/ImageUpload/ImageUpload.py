
# import sublime*
import sublime, sublime_plugin
# import system or core
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# import user-code
from ImageUpload.utils.clipboard import getClipboardImage
from ImageUpload.utils.format import format_markdown_img
from ImageUpload.utils.upload import upload

# method
def mkFormatShootImage():
	tmp_path= getClipboardImage()
	if tmp_path:
		qiniu_url= upload(tmp_path, is_delete= True)
		return format_markdown_img(qiniu_url)
	else:
		return None


# class for sublime
class ShootImageUploadForMarkdownCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, self.view.sel()[0].begin(), mkFormatShootImage())

