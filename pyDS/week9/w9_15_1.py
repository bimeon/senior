import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import warnings
warnings.filterwarnings(action='ignore')
import collections

# 데이터 불러오기
movie_df = pd.read_csv('movies.csv') # 영화 정보 데이터
cinemas_df = pd.read_csv('cinemas.csv') # 영화관 정보 데이터
transactions_df = pd.read_csv('transactions.csv') # 영화 거래 내역 데이터
customers_df = pd.read_csv('customers.csv') # 고객 정보 데이터


#문제1-1
# cinema_id를 기준으로 transaction_df와 cinema_df의 필요한 열 합치기
transaction_and_cinema_df = pd.merge(transactions_df[['transaction_id', 'cinema_id', 'movie_id', 'ticket_sales']], cinemas_df[['cinema_id', 'region']], on='cinema_id', how='left')
# movie_id를 기준으로 위의 df와 movie_df의 필요한 열 합치기
popular_movie_genre_df = pd.merge(transaction_and_cinema_df, movie_df[['movie_id', 'genre']], on='movie_id', how='left')

# category_region_movie_df = popular_movie_genre_df.groupby('region')['genre'].reset_index(name='genre')
category_region_movie_df = popular_movie_genre_df.groupby(by = ['region', 'genre'], as_index = False).sum()
# region_and_genre_df = category_region_movie_df[['region', 'genre']]
print(category_region_movie_df.head(10))

# genre의 열에 들어간 값들을 , 를 기준으로 split 하여 별개의 열로 저장
# ticket_sales를 기반으로 sum() 하기 -> 가장 높은 값을 가진 것이 선호도가 높을 것
# region 기준으로 group by하기

# #bar plot을 활용하여, 지역별 장르 선호도 비교 시각화
#sns.barplot(x="region", y="category_region_movie_df", data = category_region_movie_df, hue='category_region_movie_df')


#문제1-2

#transaction_id를 기준으로 transaction_df와 customers_df 합치기
customer_transactions_df = pd.merge(customers_df, transactions_df[['transaction_id', 'movie_id']], on='transaction_id', how='left')
#movie_id를 기준으로 customer_transactions_df과 movie_df 합치기
customer_transactions_movies_df = pd.merge(customer_transactions_df, movie_df[['movie_id', 'title']], on='movie_id', how='left')

#연령대에 따른 영화 선호도차이를 구하기 위해 연령대로 묶고 영화 개수 count
summary = customer_transactions_movies_df[['age_group', 'title', 'transaction_id']].groupby(by = ['age_group', 'title'], as_index = False).count()

#heatmap으로 나타내기 위해 pivot_table로 전환
pivot_df = summary.pivot_table(index = 'title', columns = 'age_group', values= 'transaction_id')

#연령대에 따른 영화 선호도 차이 heatmap으로 나타내기
fig = plt.figure()
fig.set_size_inches(15, 15)
sns.heatmap(pivot_df, annot=True)
plt.title('Movies by Age Group', fontsize=20)
plt.show()


#문제1-3
## 데이터 결합
# 거래 내역과 고객을 transaction_id를 기준으로 결합
merged_df = pd.merge(customers_df, transactions_df, on='transaction_id', how='left')

## 나이대 별로 그룹 만들기
# groupby로 구매 채널과 나이대를 고려한 데이터 값 확인하기
df_count = merged_df.groupby(["age_group", "purchase_channel"]).count()

## 그래프 출력
# index = 연령대
index = ['Teens', '20s', '30s', '40s', '50s+']
# 막대 : Mobile, Offline, Online 채널별 구매
# groupby로 데이터 값 파악한 뒤 각 채널별로 데이터 값을 리스트로 생성
Mobile = [71, 82, 64, 66, 59]
Offline = [69, 79, 63, 60, 67]
Online = [66, 64, 63, 61, 66]

# 그래프를 그리기 위해 각 데이터를 데이터프레임으로 결합
df = pd.DataFrame({'Mobile': Mobile, 'Online': Online, 'Offline': Offline}, index=index)
df.plot(kind="bar", stacked=True, figsize=(15, 10))
plt.show()

### 문제 1-4
## 데이터 확인하기
# 시간대 구분하기
# 시간대 값의 분포를 확인하기
time_check = merged_df['time'].unique()

# 시간대별 연령대 분포 데이터를 파악하기 위해 groupby 사용
df_count3 = merged_df.groupby(["age_group", "time"]).count()

## 연령별 구분하기
# 주어진 조건으로 인덱스 생성
index = ['10-13시', '13-16시', '16-19시', '19-22시']
# groupby로 파악한 데이터를 수기로 입력하여 데이터 프레임 생성
# 데이터를 이해하기 쉽도록 연령대 순서대로 teens부터 정렬
Teens = [59, 42, 57, 41]
age_20s = [63, 51, 46, 58]
age_30s = [50, 42, 45, 53]
age_40s = [52, 41, 35, 59]
age_50s = [54, 40, 38, 60]

# 그래프에 들어갈 연령대를 순서에 맞게 정렬하고 연령대별 해당하는 데이터 입력
df_ageband = pd.DataFrame({'Teens': Teens, '20s': age_20s, '30s': age_30s, '40s': age_40s, '50s+': age_50s},
                          index=index)

# line plot 으로 그래프를 생성하고 'o'모양의 마커 생성
df_ageband.plot(kind="line", figsize=(15, 10), marker='o')

# tick에따라 격자무늬 생성
plt.grid(True)

# 그래프 나타내기
plt.show()