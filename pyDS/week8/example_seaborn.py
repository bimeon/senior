import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('../week6/data/adult.data', header=None)
df.columns = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marrital-status', 'occupation', 'relationship',
              'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'wage']

df.age.head().plot(kind='bar')
plt.show()

df.age[1:100].plot.hist()
plt.show()

df[['age']].boxplot()
plt.show()

sns.set()
df2 = df[['age', 'capital-gain', 'hours-per-week']]
sns.pairplot(df2)
plt.show()