#Created by Conor Henson 
z = 0
for i in range(100, 999):
	for j in range(100, 999):
		x = str(i * j)
		if x[0:3] == x[:2:-1]:
			if x > z:
				z = x
print z


