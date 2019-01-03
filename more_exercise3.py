#question 3
password = raw_input("Enter a password")
if len(password) > 6 and len(password) < 16 and "$" in password and "2" in password or "8" in password and "A" in password or "Z" in password:
    print "Strong Password"
else:
    print "Weak Password"

#question 4
number_1 = int(raw_input("Enter first number"))
number_2 = int(raw_input("Enter second number"))
number_3 = int(raw_input("Enter third number"))


if number_1 > number_2 and number_1 > number_3:
    print number_1
elif number_2 > number_1 and number_2 > number_3:
    print number_2
elif number_3 > number_1 and number_3 > number_2:
    print number_3 

#question 5
user_number = int(raw_input("Enter any number to know the factorial of that number"))
i = 1
factorial = 1
while i <= user_number:
    factorial = factorial * i
    i = i + 1
print factorial

