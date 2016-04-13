
# object
i= 1
print i

# line
i= 'one line'; print 'Multi command in one line: ',i
i= 'backslash\
 new line'
print i

# indent
i= 'indent'
#	print i

# calc
print '10//3=',10//3, '\t5&3=',  5&3, '\t~5=-(5+1)', ~5,' \tnot i', not i

# priority
print not 2-1, not 1, not 0

# input+ if/elif/else
# i= int(raw_input("input a num:"))
if i == 0:
	print 'zero is good'
elif i< 0:
	print 'below zero'
else:
	print 'nice'

# while
i= 1
s= ''
time=0
while True:
	s+= `i`
	time += 1
	if time> 2:
		break
	else:
		continue
else:
	s+= '0'
print s

# for
i= 1
s= ''
for i in range(1, 10):
	s+= `i`
else:
	s+= ''
print s

