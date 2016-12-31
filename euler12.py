#Created by Conor Henson 
def triangle_numbers(numOfDiv):
	num = num1 = 76576499
	count = 0
	while count < numOfDiv:
		count = 0
		num = (num1 * (num1 +1))/2
		div = 1
		while div <= num *.5:
			if num % div == 0:
				count += 1
			div += 1
			print div, count

		num1 += 1
	return num


print triangle_numbers(500)

			
