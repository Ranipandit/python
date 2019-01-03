#part1
def calculator(number_x,number_y,operation):
    if operation == "add":
        return number_x + number_y
    elif operation == "subtract":
        return number_x - number_y
    elif operation == "multiply":
        return number_x * number_y
    elif operation == "divide":
        return number_x / number_y

number_1 = calculator(24,20,"add")
number_2 = calculator(50,60,"multiply")
number_3 = calculator(80,120,"divide")
number_4 = calculator(90,23,"subtract")
print number_1
print number_2
print number_3
print number_4

#part2
def calculator(number_x,number_y,operation):
    if operation == "add":
        return number_x + number_y
    elif operation == "subtract":
        return number_x - number_y
    elif operation == "multiply":
        return number_x * number_y
    elif operation == "divide":
        return number_x / number_y

number_1 = int(raw_input("Enter number "))
number_2 = int(raw_input("Enter another number"))

add_result      = calculator(number_1,number_2,"add")
subtract_result = calculator(number_1,number_2,"subtract")
multiply_result = calculator(number_1,number_2,"multiply")
divide_result   = calculator(number_1,number_2,"divide")

print add_result
print subtract_result
print multiply_result
print divide_result

#part3
def list_change(list1,list2):
    counter = 0
    new_list = []
    while counter < len(list1):
        multiple = calculator(list1[counter],list2[counter],"multiply")
        new_list.append(multiple)
        counter = counter + 1
    return new_list

multiple_list = list_change([5, 10, 50, 20],[2, 20, 3, 5])
print multiple_list


