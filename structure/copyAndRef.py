
argList= [1, 2, 3, 4]
refList= argList		# ref
copyList= argList[:]	# copy

print argList, refList, copyList
del refList[0]
del copyList[3]
print argList, refList, copyList

