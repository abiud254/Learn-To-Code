# Create a pythagoras theorem calculator that asks for the width and height of triangle and returns the hypotenuse

side_a = int(input("What is the width of the triangle? "))
side_b = int(input("What is the height of the triangle? "))
hypotenuse = (side_a**2 + pow(side_b, 2)) ** (1 / 2)
print("The hypotenuse of the triangle is", round(hypotenuse, 2))
