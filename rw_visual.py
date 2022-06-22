# import sys
# impoprt os
# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:

    rw = RandomWalk()
    rw.fill_walk()
    plt.style.use('classic')
    fig, aix = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    # aix.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
    # aix.scatter(0, 0, c='green', edgecolors='none', s=100)
    # aix.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    aix.plot(rw.x_values, rw.y_values, linewidth=5, color='red')
    aix.get_xaxis().set_visible(False)
    aix.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input('make another walk (y/n): ')
    if keep_running == 'n':
        break
