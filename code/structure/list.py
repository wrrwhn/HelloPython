

argList= ['arg1', 'arg2', 3]

print argList, len(argList)

argList.append('arg3')
print argList
# for arg in argList:
# 	print '\t', arg

del argList[0]
print argList

# create list by oldList
print [ 'new_'+i for i in argList if len(str(i))> 1]
