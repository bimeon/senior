import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

# MATLAB interface
fig_1 = plt.figure()
plt.subplot(2, 1, 1)
plt.plot(x, np.sin(x))
plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x))

fig_1.savefig('example_interface_matplot.png')

# OOP interface
fig_2, ax = plt.subplots(2)
ax[0].plot(x, np.sin(x))
ax[1].plot(x, np.cos(x))

fig_2.savefig('example_interface_oop.png')