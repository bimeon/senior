import matplotlib.pyplot as plt
import numpy as np

rng = np.random.RandomState(0)

fig = plt.figure()

for marker in ['o', '.', 'h', 'x', '+', 'v', '^']:
    plt.plot(rng.rand(5), rng.rand(5), marker,
             markersize=10, markeredgewidth=2,
             markerfacecolor='blue', markeredgecolor='black',
             label="marker='{0}'".format(marker))
    plt.legend(numpoints=1)
    plt.xlim(0, 1.8)

fig.savefig('example_scatter.png')
plt.show()