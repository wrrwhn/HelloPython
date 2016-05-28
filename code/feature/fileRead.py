
# init
content= '''\
line 1
line 2
'''

# create file
f= file('output.txt', 'w')
f.write(content)
f.close()

# read and print
f= file('output.txt')
while True:
	line = f.readline()
	if 0== len(line):
		break
	else:
		print line
f.close()