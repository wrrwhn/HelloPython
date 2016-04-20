import sublime, sublime_plugin
import ImageGrab as grab

class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		
		# # init
		# url= 'https://g.co/ev/2334'
		# cursor= self.view.sel()[0].begin()

		# read clipborad pic
		self.view.insert(edit, cursor, pics)
		
		# # insert
		# self.view.insert(edit, cursor, "![]({url})".format(url=url))

		# # reset cursor position
		# cursor+= 2
		# self.view.sel().clear()
		# self.view.sel().add(cursor)

