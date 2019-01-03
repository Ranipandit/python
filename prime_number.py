number = 2

while number < 100:
    even = number/2
    odd = number/3
    if number % 2 == 0 or number % 3 == 0:
        print number,"is not a prime number"
    else:
        print number,"is a prime number"
    number = number + 1 

