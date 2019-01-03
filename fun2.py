# funtion-question 2
def function_print_lines(name,description):
    print name
    print description
function_print_lines("Mera Naam Rishab hai","Mai NavGurukul ka founder hu")

# function-question 3

#part1

def add_numbers(number1,number2):
    total_sum = number1 + number2
    print "Dono number ka sum",total_sum,"hai"

add_numbers(50,30)

#part2

def add_numbers_list(list1,list2):
    counter = 0
    while counter < len(list1):
        total_sum = list1[counter] + list2[counter]
        print total_sum
        print "---------------"
        counter = counter + 1
add_numbers_list([20,13,30],[30,20,40])        