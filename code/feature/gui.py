
# import
# Tkinter
	# http://www.runoob.com/python/python-gui-tkinter.html
	# https://wiki.python.org/moin/TkInter
	# https://docs.python.org/2/library/tkinter.html
# wxPython
# Jython

import Tkinter as tk

# def
class Application(tk.Frame):
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.grid()
		self.createWidgets()

	def createWidgets(self):
		self.quitButton= tk.Button(self, text='Quit', command=self.quit)
		self.quitButton.grid()


# use
app= Application()
app.master.title("Minimal Application")
app.mainloop()