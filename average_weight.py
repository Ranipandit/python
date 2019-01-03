counter = 1
sum = 0
while counter<=11:
	weight = int(raw_input("enter your weight > "))
	sum = sum + weight
	counter = counter + 1
average_weight = sum /counter
print sum 
print "Aap sab ka average weight hai",average_weight
if average_weight % 5 == 0:
	print average_weight
