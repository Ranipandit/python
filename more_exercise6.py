#question 6
def change_list(string_list):
    new_list = []
    counter = 0
    while counter < len(string_list):
        if string_list[counter] not in new_list:
            new_list.append(string_list[counter])
        counter = counter + 1
    return new_list

list1 = change_list(["Empathy", "Empathy", "Kindness", "Kindness", "Compassion", "Humble", "Humble"])
print list1

#question 7
def check_list(list1,list2):
    counter = 0
    new_list = []
    while counter < len(list1):
        count = 0
        while count < len(list2):
            if list1[counter] == list2[count]:
                new_list.append(list1[counter])
            count = count + 1
        counter = counter + 1
    return new_list

check_number_list = check_list([1, 342, 75, 23, 98,12],[75, 23, 98, 12, 78, 10, 1])
print check_number_list


