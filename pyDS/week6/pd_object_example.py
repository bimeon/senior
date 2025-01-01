import pandas as pd

list_1 = ['송이', 11, '푸들']
series_1 = pd.Series(list_1, index=['name', 'age', 'breed'])

dict_1 = {'name': '몽자', 'age': 4, 'breed': '푸들'}
series_2 = pd.Series(dict_1)

print(series_1, series_2, sep='\n')

df_1 = pd.DataFrame((series_1, series_2))
print(df_1)