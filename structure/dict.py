
dic={
	"a": 1,
	"b": 2,
	"c": 3,
	"d": 4
}
print dic, dic['a']

dic['f']= 5
del dic['f']
print dic, len(dic)

for key, val in dic.items():
	print 'dic[%s]= %d' %(key, val)

if 'e' in dic:
	print 'e in the dict'
else:
	print 'e not in the dict'