import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# csv 파일 불러오기
movies = pd.read_csv('movies.csv') # 영화의 고유 식별자, 영화 제목, 영화의 장르들
cinema = pd.read_csv('cinemas.csv') # 영화관의 고유 식별자, 영화관이 위치한 지역, 영화관이 위치한 도시/구
transaction = pd.read_csv('transactions.csv')
# 거래의 고유 식별자, 영화관의 고유 식별자, 영화의 고유 식별자, 구매한 티켓수, 거래 날짜, 영화 상영 시간,구매 채널
customer = pd.read_csv('customers.csv')
# 거래의 고유 식별자, 구매자의 나이대, 영화의 고유 식별자

# 1번
# movie의 genre 부분 분리하기
movie_splited = movies['genre'].str.split(',', expand=True)
new_movie_splited = pd.concat([movies, movie_splited], axis=1)
# print(new_movie_splited.head()

# 각 장르에서 유니크한 값 뽑아내기
genre_1 = new_movie_splited[0].unique().tolist()
genre_2 = new_movie_splited[1].unique().tolist()
genre_3 = new_movie_splited[2].unique().tolist()

# 3개의 칼럼 합쳐서 중복값 삭제하기
genre = set(genre_1+genre_2+genre_3)


# 거래데이터와 영화관 정보를 cinema id를 기준으로 결합 (left join)
merged_df = pd.merge(transaction, cinema, on='cinema_id', how='left')

# merged_df와 new_movie_splited 데이터를 movie_id를 기준으로 결합 (left join)
merged = pd.merge(merged_df, new_movie_splited, on='movie_id', how='left')

# cinema, movies, transaction 파일을 다 합친 최종 df인 merged의 모든 컬럼 확인용
pd.set_option('display.max_columns', None) # 전체 열 보기


#print(merged.head())

# region과 분리한 genre(0,1,2)만 가지고 df 만들기
df = merged[['region',0,1,2]]
print(df.head())

# region별로 genre의 갯수 count
df.groupby('region')


#1-2. 연령대에 따른 영화 선호도 차이
# 데이터들을 불러옴
age_movie_df = pd.DataFrame()
# movies 데이터와 transaction 데이터를 movie_id 기준으로 새로운 merged_movies_transaction로 묶음
merged_movies_transaction = pd.merge(movies, transaction, on='movie_id', how='left')

# merged_movies_transaction 데이터와 customer 데이터를 새로운 merged_transaction_customer로 묶음
merged_transaction_customer = pd.merge(merged_movies_transaction, customer, on='transaction_id', how='left')

# 필요한 데이터만 추출하기
#merged_transaction_customer = merged_transaction_customer[['title','age_group']]

# merged_transaction_customer 데이터에서 title과 age_group만 따로 분리해서 새로운 age_movie_df로 만듦
# age_movie_df = merged_transaction_customer[['title', 'age_group']]
# title과 age_group을 기준으로 나눈 뒤 count()
age_movie_df = merged_transaction_customer.groupby(['title']).count()
print(age_movie_df)


# 히트맵 제목, x축, y축 작성
plt.title("Movies by Age Group")
plt.xlabel('age_group')
plt.ylabel('title')

# heatmap 제작
sns.heatmap(age_movie_df,annot=True, fmt='d')
plt.show()

# 1-3번 : 나잇대별 구매 채널 시각화
merge_data = pd.merge(transaction, customer, how='inner', on=None) # 두 데이터를 합치기
# 필요한 데이터만 추출하기
channel_efficiency_data = merge_data[['age_group','purchase_channel']]

# 두개로 그룹화해서 숫자 세기
data_count = channel_efficiency_data.groupby(['age_group','purchase_channel'])['purchase_channel'].count()
data_count = data_count.T.unstack().reset_index() # 데이터 형태로 바꾸기
unique_age = data_count['age_group'].unique()

# stacked bar 차트 그리기
data_count.plot(x='age_group',kind='bar',stacked=True) # bar 차트 그리기
plt.xlabel('age_group')         # x축 레이블 설정
plt.title('Purchase Channel by Age Group')  # 제목 설정
plt.legend(loc='upper right')                   # 범례 추가
plt.show()


#1-4.4개의 시간 구분에 따른 방문자 수 시각화

# 각각의 영화를 시간대 4개로 나눠서 구분

# 연령대 별 방문횟수 -> 연령별로 그룹화한 후에 시간대별로 count함

# line plot 으로 시간대별 그래프 그림