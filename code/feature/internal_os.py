
import os

print os.name 			#windows= nt, linux/unix= posix
print os.getcwd()		# pwd
print os.getenv('path') 		# os.putenv
print os.listdir('C:\\adb') 		
f = file("tmp.txt", 'w')
f.write("new")
f.close()
# print os.remove('tmp.txt')
# print os.system("time")
# print os.linesep 		# windows= \r\n, linux=\n, mac=\r
print os.path.split('C:\\adb\\flash-all.bat')
print os.path.isfile('tmp.txt')
