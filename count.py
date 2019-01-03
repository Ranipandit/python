numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
counter =  0
count = 0

while counter < len(numbers):
    if numbers[counter]>20 and numbers[counter]<40:
        count = count + 1
        print count
    counter =  counter + 1
