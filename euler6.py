#Created by Conor Henson 
from math import * 
x = 100
xSquared = 0
xSumSquared = 0
for i in xrange(1, x + 1):
	xSquared += i ** 2
	xSumSquared += i

print xSumSquared ** 2 - xSquared