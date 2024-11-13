import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw=RandomWalk()
rw.fill_walk()

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
point_numbers=range(rw.num_points)
ax.scatter(rw.x_value, rw.y_value, c=point_numbers,cmap=plt.cm.Blues, edgecolors='none',s=15)
ax.scatter(0, 0, c='green', edgecolors='none', s=100)
ax.scatter(rw.x_value[-1], rw.y_value[-1], c='red', edgecolors='none',s=100)
ax.set_aspect('equal')
plt.show()
