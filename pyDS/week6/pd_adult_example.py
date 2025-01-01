import pandas as pd

df = pd.read_csv('data/adult.data', header=None)
pd.set_option('display.max_columns', None)

print('>> data basics')
print(df.size, df.shape, df.dtypes, df.columns)
df.columns = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marrital-status', 'occupation', 'relationship',
              'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']
print(df.columns, df.head(), df.tail(), sep='\n')

print('>> data summary')
print(df.describe())

print('>> details')
print(df.education.unique())
print(df.education.value_counts())
print(df['capital-gain'].value_counts())
print(df.groupby(['income']).age.mean())
print(df.groupby(['income']).age.std())
print(df['capital-gain'].corr(df['age']))