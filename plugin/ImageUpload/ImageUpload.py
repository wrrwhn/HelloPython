
# import system or core
import sublime, sublime_plugin
# from sys import path
# path.append('C:/Users/Administrator/AppData/Roaming/Sublime Text 3/Packages/ImageUpload/utils/clipboard.py')
# path.append('C:/Users/Administrator/AppData/Roaming/Sublime Text 3/Packages/ImageUpload/utils/format.py')
# path.append('C:/Users/Administrator/AppData/Roaming/Sublime Text 3/Packages/ImageUpload/utils/upload.py')

# import user-code
from ImageUpload.utils.clipboard import getClipboardImage
from ImageUpload.utils.format import format_markdown_img
from ImageUpload.utils.upload import upload

# methon
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

