import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
features = iris.data.T

fig = plt.figure()

plt.scatter(features[0], features[1], alpha=0.2,
            s=100*features[3], c=iris.target, cmap='viridis')

plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.colorbar()

fig.savefig('example_iris.png')
plt.show()