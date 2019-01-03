def check_unique_numbers(list1,list2):
    counter =  0
    new_list = []
    while counter < len(list1):
        count = 0
        if list1[counter] not in new_list:
            new_list.append(list1[counter])
            while count < len(list2):
                if list2[count] not in new_list:
                    new_list.append(list2[count])
                count = count + 1
        counter = counter + 1
    return new_list

check_list = check_unique_numbers([1, 5, 10, 12, 16, 20],[1, 2, 10, 13, 16])
print check_list
