import pandas as pd
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

store_df = pd.read_csv('problem 1/stores_df.csv')
order_1_df = pd.read_csv('problem 1/orders_1_df.csv')
order_2_df = pd.read_csv('problem 1/orders_2_df.csv')
review_df = pd.read_csv('problem 1/review_df.csv')

# 문제 1-1
# 카테고리 결측치 처리
store_df["category"].fillna('etc', inplace=True)

# 가장 자주 등장하는 지역으로 채우기
most_frequent_area = str(store_df["area"].mode()[0])
store_df["area"].fillna(most_frequent_area, inplace=True)

# order_1_df, order_2_df를 결합 (상하반기 order_df 결합)
order_df = pd.concat([order_1_df, order_2_df])

# store와 oreder df를 store_id 기준으로 결합
store_order_df = pd.merge(left = store_df, right = order_df, how="inner", on="store_id")

# "order_amount", "category" 만 추출
store_order_df_filter = store_order_df[["order_amount", "category"]]
# 카테고리별 평균 주문 금액 구하기
mean_order_amount = round(store_order_df_filter.groupby("category").mean(), 2)
print(mean_order_amount)

# "order_date", "category"
store_order_df_filter = store_order_df[["order_date", "category"]]
# category별로 groupby하기
mean_daily_order = store_order_df_filter.groupby("category")
# 일별로 groupby하기
# mean_order_amount와 합치기



# 문제 1-2
# 리뷰 데이터의 결측치를 'No Comments'로 채워넣기
review_df_fillnan = review_df.fillna('No Comments')

# review_df_nan을 리스트로 변환
review_texts = review_df_fillnan['review_text'].to_list()
# 단어 저장 리스트 생성
word_list = []
# for문을 돌면서 각 리뷰에 대해 word_list에 단어들을 append
for review in review_texts:
    word_list.append(review.split())

# 2차원 리스트를 1차원으로 변환
word_list_1d = sum(word_list, [])
# 단어 개수 세기
word_counts = Counter(word_list_1d)
# 가장 많이 나온 50개 지정
tags = word_counts.most_common(50)

# 워드클라우드 생성
wc = WordCloud(background_color="white", max_font_size=60)
cloud = wc.generate_from_frequencies(dict(tags))

# plt에서 워드클라우드 보여주기
plt.figure(figsize=(10, 8))
plt.axis('off')
plt.imshow(cloud)
plt.show()

# order_df과 revier_df를 order_id를 기준으로 합치기
df_total = pd.merge(left = order_df, right = review_df, how="inner", on="order_id")
# 필요한 열만 남기기 (order_amount, delivery_time, rating)
df_total_filter = df_total[["order_amount", "delivery_time", "rating"]]
# 상관관계 구하기
print(df_total_filter.corr(method='pearson'))