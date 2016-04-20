import sublime, sublime_plugin
import ImageGrab as grab

class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		
		# # init
		# url= 'https://g.co/ev/2334'
		# cursor= self.view.sel()[0].begin()

		# read clipborad pic
		pics= grab.grabclipboard()
		self.view.insert(edit, cursor, pics)
		
		# # insert
		# self.view.insert(edit, cursor, "![]({url})".format(url=url))

		# # reset cursor position
		# cursor+= 2
		# self.view.sel().clear()
		# self.view.sel().add(cursor)



# read config
# read clipboard
	# [Pillow 下载](https://pypi.python.org/pypi/Pillow)
	# [Pillow 文档](https://pillow.readthedocs.org/en/3.2.x/index.html)
# ~~setup keyNote~~
	# sublime-keymap User
# save pic
# update to qiniu thread
# ~~insert url-format~~
	# format
# ~~reset cursor position~~
	# self.view.sel()