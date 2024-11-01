import matplotlib.pyplot as plt

# data
x = [i for i in range(0, 11)]
y = [y**2 for y in x]

# plot
plt.plot(x, y)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()
