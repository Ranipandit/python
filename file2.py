batch1_students = ["Shivam", "Rahul", "Kavay", "Dhannu", "Deepanshu", "Nitin", "Manoj", "Shakrudin", "Tara", "Suraj", "Krishna"]
students_file = open("navgurukul_students.html", "w")
students_file.write("<html>\n")
students_file.write("<head>\n")
students_file.write("<title>NavGurukul Students</title>\n")
students_file.write("</head>\n")
students_file.write("<body>\n")
students_file.write("<ul>")
for student in batch1_students:
    students_file.write("<li>" + student + "</li>\n")
students_file.write("</ul>\n")
students_file.write("</body>\n")
students_file.write("</html>\n")
print students_file
students_file.close()

#####################
my_file3 = open("test_file.txt", "w")
my_file3.write("Yahan main kuch likha")
my_file3.write("\nYaha maine kuch aur bhi likha.")
my_file3.close()
my_file3.write("Kuch aur likhte hain")

