# create a "shouter" function that takes 2 arguments: a string and a number
# the function should print the string multiple times (whatever is specified in the number argument)
# capitalise every letter that is printed
# if the number is greater than 10, don't print the string, instead print "you are too loud" once
# the function should also return the string "done" and have default values


def shout(word="Hello", repetition_amount=2):
    if repetition_amount <= 10:
        for i in range(repetition_amount):
            print(word.upper())
    else:
        print("You are too loud")

    return "Done"


shout("true", 5)
