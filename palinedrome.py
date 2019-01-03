
word = raw_input("Enter any word in English >")

counter = 0
original_word = ""
opposite_word = ""


while counter < len(word):
    original_word = original_word + word[counter]
    counter = counter + 1
    length = len(word) - counter
    opposite_word = opposite_word + word[length]

if opposite_word == original_word:
    print "Palinedrome hai"
else:
    print "Palinedrome nahi hai"
	
	
	 
