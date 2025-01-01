import pandas as pd

series_1 = pd.Series({'name': '몽자', 'age': 4, 'breed': '푸들'})
series_2 = pd.Series({'name': '송이', 'age': 11, 'breed': '푸들'})
df_1 = pd.DataFrame((series_1, series_2))

print(df_1['name'], df_1.name, sep='\n')
print(df_1[0:1], df_1.loc[0:1], df_1.iloc[0:1], sep='\n')