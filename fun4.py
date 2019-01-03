#part1
def check_numbers(number1,number2):
    if number1 % 2 == 0 and number2 % 2 == 0:
        print "Dono numbers even hai"
    else: 
        print "Dono numbers even nahi hai"


#part2
def check_numbers_list(list1,list2):
    counter = 0
    while counter < len(list1):
        check_numbers(list1[counter],list2[counter])
        counter = counter + 1

check_numbers_list([2,3,4,5,7,86,98],[4,46,68,44,24,70,98])