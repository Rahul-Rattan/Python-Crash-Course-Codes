import matplotlib.pyplot as plt

values=[1,2,3,4,5]
squares=[1,4,9,16,25]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(values, squares, s=200)

#Set the title and labels
ax.set_title("Square Numbers", fontsize=14)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Values", fontsize=14)
ax.tick_params(labelsize=14)

plt.show()
