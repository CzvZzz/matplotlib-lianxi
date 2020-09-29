import matplotlib.pyplot as plt

x_values = list(range(1, 6))
y_values = [x**3 for x in x_values ]

plt.scatter(x_values, y_values, s=40)

plt.title("S N", fontsize=24)
plt.xlabel("value", fontsize=14)
plt.ylabel("S of value", fontsize=14)

plt.show()