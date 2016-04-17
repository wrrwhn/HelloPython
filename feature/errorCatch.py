
import sys

# error define
class ShortArgsException(Exception):
	def __init__(self, length, atleast):
		Exception.__init__(self)
		self.length= length
		self.atleast= atleast

# run
try:
	s = raw_input('Input:')
	if(3> len(s)):
		raise ShortArgsException(len(s), 3)
	# pass
except EOFError:
	print '\nEOF error'
	sys.exit()
except ShortArgsException, x:
	print '%d/%d'% (x.length, x.atleast)
except:
	print '\nSome error'
else:
	print '\nEveryThing goes well'
finally:
	print '\nDo some finally'