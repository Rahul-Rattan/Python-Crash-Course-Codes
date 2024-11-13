import matplotlib.pyplot as plt

x_values=range(1,1001)
y_values=[x*x for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
ax.set_title("Square Values", fontsize=14)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Squares", fontsize=14)

ax.tick_params(labelsize=10)
ax.axis([0,1100,0,1100000])
ax.ticklabel_format(style='plain')
plt.show()