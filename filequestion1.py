## question 1 and question 2
people_list=["rishabh - meerut","imtiyaz - delhi","nilima - cochin","rati - shimla","ayishah - delhi","raghu - shimla",
            "naseer - kanpur","karthikeyan - delhi","salma - jaipur","pankaj - delhi","brijesh - delhi",
            "govind - delhi","puneet - shimla","siddhi - delhi","suman - jaipur","rajeev - shimla",
            "mohinder - delhi","rajendra - jaipur","priyanka - shimla","neela - delhi","sashi - jaipur",
            "sarika - delhi","deepti - shimla","harshad - delhi","trishna - raipur","pradeep - jaipur",
            "sekhar - delhi","nand - delhi","anoop - delhi","balwinder - tokyo"]

people_place_file = open("people_place.txt","w")

for people in people_list:
    people_place_file.write(people + "\n")
people_place_file.close()

### question 3

banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]

bank_file = open("file-question3.txt","w")

for banks in banks_list:
    bank_file.write(banks+"\n")
bank_file.close()
