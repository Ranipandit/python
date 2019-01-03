def check_max_number(marks):
    big_list_length = len(marks)
    counter = 0
    while counter < big_list_length:
        small_list_length = len(marks[counter])
        maximum = 0
        count = 0
        while count < small_list_length:
            if marks[counter][count] > maximum:
                maximum = marks[counter][count]
            count = count + 1
        print maximum
        counter =  counter + 1

check_max_number([[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]])
