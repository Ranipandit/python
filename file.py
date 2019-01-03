my_file = open("people.txt")
file_data = my_file.read()
print file_data
my_file.close()

#############
my_file2 = open("people.txt2","w")
my_file2.write("Abhishek - Gurgoan\n")
my_file2.write("Ranveer - Delhi")
print my_file2
my_file2.close

##############
my_file3 = open("people3.txt", "w")
my_file3.write("Abhishek - Gurgaon\n")
my_file3.write("Ranveer - Delhi")
my_file3.write("Abhishek - Gurgaon\nRanveer - Delhi")
print my_file3
my_file3.close()