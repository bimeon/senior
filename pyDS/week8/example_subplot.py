import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

fig = plt.figure()

plt.style.use('classic')

for i in range(1, 7):
    plt.subplot(2, 3, i)
    plt.plot(x, np.sin(x), label='sin')
    plt.title('A subplot graph')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.text(5, 0, str((2, 3, i)), fontsize=10, ha='center')
    plt.legend(loc='upper right', frameon=True)
    plt.axis('equal')

fig.savefig('example_subplot.png')
plt.show()