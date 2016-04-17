

# [Python lambda](http://www.cnblogs.com/evening/archive/2012/03/29/2423554.html)

sequence= [2, 18, 9, 22, 17, 24, 8, 12, 27]

print filter(lambda x: x% 3== 0, sequence)
print map(lambda x: x* 2, sequence)
print reduce(lambda x, y: x+ y, sequence)