def break_into_words(sentence):
    counter =  0
    word = ""
    new_list = []
    while counter < len(sentence):
        word = word + sentence[counter]
        if sentence[counter] == " ":
            new_list.append(word)
            word = ""
        counter = counter + 1
    if word:
        new_list.append(word)
    return new_list

split_function = break_into_words("NavGurukul is an alternative to higher education reducing the barriers of current formal education system")
print split_function


        
