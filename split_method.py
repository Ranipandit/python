def splitMethod(sentence,character):
    new_list = []
    word = ""
    counter = 0
    while counter < len(sentence):
        word = word + sentence[counter]
        new_word = ""
        if character in word:
            length = len(character)
            new_word = new_word + word[:-length]
            new_list.append(new_word)
            word = ""
        counter = counter + 1
    new_list.append(word)
    return new_list

print splitMethod("My rani name is rani.My favourite rani game is rani Kho-kho.","rani")