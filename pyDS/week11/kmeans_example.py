import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

df = pd.read_csv("wine/wine.data", header=None)
data = df.values
X = data[:, 1:]
print(df.shape, data.shape, X.shape)

estimator = KMeans(n_clusters=5).fit(X)
y = estimator.predict(X)
print(estimator.cluster_centers_)
print(estimator.labels_)
print(y)

df_g = pd.DataFrame(X)
df_g['label'] = pd.Series(y)

sns.set(style='ticks', color_codes=True)
sns.pairplot(df_g, hue='label')
plt.show()