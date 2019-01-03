question_list = ["1--Who is the current PM(prime minister) of India","2--Which is the largest river in India",
                "3--What is the capital of India","4--Which is the largest animal on land",
                "5--Which is the largest vegetables"]

first_option  = ["1.Rajiv Gandhi","1.Ganga","1.Bhopal","1.Giraffe","1.Yam"]
second_option = ["2.Narendra Modi","2.Yamuna","2.Chandigarh","2.Zebra","2.Sweet Potato"]
third_option  = ["3.Manmohan Singh","3.Brahmaputra","3.Jaipur","3.Elephant","3.Watermelon"]
fourth_option = ["4.Chandra Shekar","4.Godavari","4.Delhi","4.Bear","4.Cabbage"]

all_options = [first_option,second_option,third_option,fourth_option]

ans_keys = [2,1,4,3,2]


# pop method to delete the last options in each list
question_list.pop()
first_option.pop()
second_option.pop()
third_option.pop()
fourth_option.pop()

# added a new question and their options in the list
question_list.append("5--What is the Capital of Telengana")
first_option.append("1.Bangalore")
second_option.append("2.Hyderabad")
third_option.append("3.Thiruvananthapuram")
fourth_option.append("4.Chennai")


index = 0
correct_answers = 0
while index < len(question_list):
    question_list_length = len(question_list[index])
    print question_list[index], " -",question_list_length
    print first_option[index]
    print second_option[index]
    print third_option[index]
    print fourth_option[index]

    user_ans = int(raw_input("Enter your ans (you have to choose one option 1,2,3 or 4 ) >"))
    if user_ans == ans_keys[index]:
        print "Congrates! apka answer sahi hai"
        correct_answers = correct_answers + 1
    else:
        print "Sadly apka answer galat hai"
    print ''
    index = index + 1
print "You answered ",correct_answers , "correct answere"