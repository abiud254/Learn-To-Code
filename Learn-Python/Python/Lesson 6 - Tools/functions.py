# create a function
def print_x_times(parameter="loop", loop_amount=5):
    counter = 0
    while counter < loop_amount:
        print(counter, parameter)
        counter += 1
    return "something else"


def hypotenuse_calculator(side_a=1, side_b=1):
    hypotenuse = (side_a**2 + side_b**2) ** (1 / 2)
    return round(hypotenuse, 2)


# call
# test = print_x_times("something", 4)
# print(test)

print(hypotenuse_calculator(side_a=5, side_b=10))
