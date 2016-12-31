#Created by Conor Henson 
import math
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return 1

x = 2
y = 0
while y < 6:
	y += is_prime(x)
	x += 1
print x - 1