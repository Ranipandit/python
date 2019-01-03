names = ["rishabh","imtiyaz","nilima","rati","ayishah","raghu","naseer","karthikeyan","salma","pankaj",
        "brijesh","govind","puneet","siddhi","suman","rajeev","mohinder","rajendra","priyanka","neela",
        "sashi","sarika","deepti","harshad","trishna","pradeep","sekhar","nand","anoop","balwinder"]

location = ["meerut","delhi","cochin","shimla","delhi","shimla","kanpur","delhi","jaipur","delhi","delhi",
        "delhi","shimla","delhi","jaipur","shimla","delhi","jaipur","shimla","delhi","jaipur","delhi",
        "shimla","delhi","raipur","jaipur","delhi","delhi","delhi","tokyo"]
 
delhi_people   = open("delhi.txt","w")
shimla_people  = open("shimla.txt","w")
other_people   = open("others.txt","w")
question4_file = open("question4_file.txt","w")
array_length = len(names)
counter = 0

while counter < array_length:
    question4_file.write(names[counter]+" - "+location[counter]+"\n")
    if "delhi" == location[counter]:
        delhi_people.write(names[counter]+" - "+location[counter]+"\n")
    elif "shimla" == location[counter]:
        shimla_people.write(names[counter]+" - "+location[counter]+"\n")
    else:
        other_people.write(names[counter]+" - "+location[counter]+"\n")
    counter = counter + 1

delhi_people.close()
shimla_people.close()
other_people.close()
question4_file.close() 