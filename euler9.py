#Created by Conor Henson 
#Very slow but works by brute force
for i in range(1, 1000):
	for j in range(1, 1000):
		for k in range(1, 1000):
			if i < j and j < k:
				if i ** 2 + j ** 2 == k ** 2 and i + j + k == 1000:
					print i * j * k

