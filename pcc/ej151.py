import matplotlib.pyplot as plt

x_values5 = range(1,6)
y_values5 = [x**3 for x in x_values5]

plt.style.use('seaborn')

fig, ax = plt.subplots()
ax.scatter(x_values5, y_values5, c = y_values5, cmap = plt.cm.hsv, s = 50)
ax.set_title("Third Power Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Third Power of Value", fontsize = 14)
ax.tick_params(axis = 'both', which = 'major', labelsize = 14)

plt.show()

x_values5k = range(1,5001)
y_values5k = [x**3 for x in x_values5k]


fig2, ax2 = plt.subplots()
ax2.scatter(x_values5k, y_values5k, c = y_values5k, cmap = plt.cm.Blues, s = 10)
ax2.set_title("Third Power Numbers", fontsize = 24)
ax2.set_xlabel("Value", fontsize = 14)
ax2.set_ylabel("Third Power of Value", fontsize = 14)
ax2.tick_params(axis = 'both', which = 'major', labelsize = 14)

plt.show()