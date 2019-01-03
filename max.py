
number = [50,40,23,70,56,12,90,5,10,7]

counter = 0
max_number = 0
while counter < len(number):
	if max_number < number[counter]:
		max_number = number[counter]
	counter = counter + 1
print max_number

