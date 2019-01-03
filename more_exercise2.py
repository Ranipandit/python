number_of_student = int(raw_input("Enter Number of Students"))
budget=int(raw_input("Enter the budget of one student"))

counter = 1
total_budget = 0
while counter <= number_of_student:
    total_budget = total_budget + budget
    counter = counter +  1
if total_budget < 50000:
    print "Hum budget ke andar"
else:
    print "Hum budget ke bahar hai"
    