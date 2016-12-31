#Created by Conor Henson 
x =1000
y = 0
for i in xrange(0,x):
	if i % 3 == 0:
		y += i
	elif i % 5 == 0:
		y += i

print y
