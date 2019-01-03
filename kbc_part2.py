question_list = ["1.Who is the current PM(prime minister) of India","2.Which is the largest river in India",
                "3.What is the capital of India","4.Which is the largest animal on land",
                "5.Which is the largest vegetables"]

first_option  = ["Rajiv Gandhi","Ganga","Bhopal","Giraffe","Yam"]
second_option = ["Narendra Modi","Yamuna","Chandigarh","Zebra","Sweet Potato"]
third_option  = ["Manmohan Singh","Brahmaputra","Jaipur","Elephant","Watermelon"]
fourth_option = ["Chandra Shekar","Godavari","Delhi","Bear","Cabbage"]

all_options = [first_option,second_option,third_option,fourth_option]

ans_keys = [0,1,2,3,4]

# pop method to delete the last options in each list
question_list.pop()
first_option.pop()
second_option.pop()
third_option.pop()
fourth_option.pop()

# third question and its all options printed
print question_list[2]
print all_options[0][2]
print all_options[1][2]
print all_options[2][2]
print all_options[3][2]

# added a new question and their options in the list
question_list.append("What is the Capital of Telengana")
first_option.append("Bangalore")
second_option.append("Hyderabad")
third_option.append("Thiruvananthapuram")
fourth_option.append("Chennai")

# printed the length of question list
print len(question_list)

# stored the second_option element in a variable
option2 = second_option[1]

print option2

