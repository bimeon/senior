import matplotlib.pyplot as plt
import numpy as np

x1 = np.random.normal(0, 0.8, 1000)
x2 = np.random.normal(-2, 1, 1000)
x3 = np.random.normal(3, 2, 1000)

fig = plt.figure()

print(plt.style.available)
plt.style.use('seaborn-v0_8-white')
kwargs = dict(histtype='stepfilled', alpha=0.3, bins=40)

plt.hist(x1, **kwargs)
plt.hist(x2, **kwargs)
plt.hist(x3, **kwargs)

fig.savefig('example_histogram.png')
plt.show()