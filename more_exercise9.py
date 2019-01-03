def is_harshad_number(number):
    first_number = number /10
    second_number = number % 10
    total = first_number + second_number
    if number % total == 0:
        return "harshad number hai"
    else:
        return "harshad number nahi hai"


count = 0
while count < 1000:
    count = count + 1
    harshad_number = is_harshad_number(count)
    print harshad_number

    
