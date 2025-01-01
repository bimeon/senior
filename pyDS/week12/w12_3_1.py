import pandas as pd
from apyori import apriori

# csv 읽어오기
customer = pd.read_csv('customer.csv')
transaction = pd.read_csv('transaction.csv')

# product 열의 값들을 transaction_id를 기준으로 하나의 list로 만들기
transaction_products = transaction.groupby('transaction_id')['product'].apply(list).reset_index(name='products')
# 기존 transaction 데이터와 merge
transaction_products_with_region = pd.merge(transaction_products, transaction, on='transaction_id', how='left')
# 필요한 열만 추출
transaction_products_final = transaction_products_with_region[['transaction_id', 'region', 'products']]

# transaction_id를 기준으로 groupby
transaction_id_grouped = transaction.groupby("transaction_id")
# 평균 금액 계산
transaction_amounts = transaction_id_grouped['amount'].agg(['mean'])

# 평균 금액과 products list가 포함된 데이터 병합
transactions_merge = pd.merge(transaction_products_final, transaction_amounts, on='transaction_id', how='left')

# 지역명 받아오기
selected_region = 'R020'

# 해당 지역에 대한 행만 추출
transaction_products_region = transactions_merge.loc[transactions_merge['region'] == selected_region]
# products list 열만 추출
transactions_df = transaction_products_region['products']
# series를 list로 변환
transactions_list = transactions_df.to_list()

# apriori 계산
results = list(apriori(transactions_list, min_support=0.2, min_confidence=0.7))

# 결과 출력
for res in results:
    print(res.ordered_statistics)

# 결과 df 만들기 - support 값을 기준으로 내림차순 한 df에서 차례대로 item set를 가져오기
# 해당 set에 해당하는 평균 값들의 합을 가져와서 base_price로 넣기
# base_price의 90% 가격을 discounted_price에 넣기