number =6
counter =1

guess = raw_input("1 se lekar 10 ke bich me koi sa bhi number guess karo > ")

while counter<=10:
	chances = 11
	chances = chances - counter
	print ""
	print "***********Aapke paas ab ", chances , " chances baki hai************"
	if int(guess) == number:
		print " Wah! Aapne sahi guess kar liya hai"
		break
	elif int(guess) > number:
		print "Badaa number hai! Ek bar aur try karo or Aap 'quit' likhkar game exist bhi kar skte ho "
		guess = raw_input(">>>> ")
		if guess == "quit":
			print ""
			print "**********Aap game ko exit kr chuke ho***********"
			break
	elif int(guess) < number:
		print "Chhota number hai! Ek bar aur try  karo or Aap 'quit' likhkar game exist bhi kar skte ho "
		guess = raw_input(">>>> ")
		if guess == "quit":
			print ""
			print "**********Aap game ko exit kr chuke ho************"
			break
	counter = counter + 1	
