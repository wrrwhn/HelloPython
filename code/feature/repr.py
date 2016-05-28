
i= []
i.append('item')

print i
print `i`
print repr(i)


class Object:
	def __init__(self, name):
		self.name= name
	def __str__(self):
		return self.name

obj= Object('yao')

print obj
print `obj`
print repr(obj)


# result
# ['item']
# ['item']
# ['item']
# yao
# <__main__.Object instance at 0x02B35198>
# <__main__.Object instance at 0x02B35198>