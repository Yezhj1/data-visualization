import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()
ax.plot([i for i in range(1, 6)], squares)
ax.set_title("2", fontsize=25)
plt.show() 