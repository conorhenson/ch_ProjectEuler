#Created by Conor Henson 
import math
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return n
summ = 0
for i in range(2000000, 1, -1):
	summ += is_prime(i)
print summ