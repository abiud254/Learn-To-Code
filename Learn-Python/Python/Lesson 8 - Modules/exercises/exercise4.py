# create a list, (1,2,3,4,5) and run code for every item in the list
# if value is 2, print "the value is 2"
# if it isn't, print "the value is not 2"
# if the value is 5, run a while loop that prints "last item" 6 times

exercise_list = [1, 2, 3, 4, 5]
exercise_counter = 0

for value in exercise_list:
    if value == 2:
        print("the value is 2")
    else:
        print("the value is not 2")
while exercise_counter < 6:
    print("last item")
    exercise_counter += 1
