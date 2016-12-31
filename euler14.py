

def collatzSeq(starting_num):
	x = y = starting_num
	seen_nums = []
	for i in range(starting_num): 
		seen_nums[i].append([])
		while x > 1:
			if x in seen_nums:
				print seen_nums.index(x)
				return 0
			elif x % 2 == 0:
				seen_nums[i][].append(x)
				x = x /2
			else:
				seen_nums[i][].append(x)
				x = (3 * x) +1
		y = y - 1
		x = y 

collatzSeq(10)
