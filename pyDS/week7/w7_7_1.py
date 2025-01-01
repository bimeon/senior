####### [ 1 - 1 ] #######
# #판다스불러오기
import pandas as pd
#
##store_df.csv, oredrs_1_df.csv,oredrs_2_df.csv 파일 불러오기##
df1 = pd.read_csv("problem 1/stores_df.csv", encoding= 'cp949')
df2 = pd.read_csv("problem 1/orders_1_df.csv", encoding= 'euc-kr')
df3 = pd.read_csv("problem 1/orders_2_df.csv", encoding= 'euc-kr')


##df1 category의 결측치 'etc'로 대체
df1['category'].fillna('etc', inplace=True)
## area의 결측치 ‘가장 자주 등장하는 지역＇으로 대체
df1['area'].fillna('가장 자주 등장하는 지역', inplace=True)


##상반기와 하반기의 주문데이터 결합##
merged_df = pd.merge(df2, df3, on= 'order_amount', how= 'outer') #outer : 두 데이터프레임의 모든 값을 결합한다

###merged_df = '{:.2f}'.format- 소수점 둘째자리 까지 구하기
#print(merged_df = '{:.2f}'.format)


######## [ 1 - 2 ] ########
#wordcloud와 collections library를 사용하기 위해서 import하였다
import pandas as pd
from wordcloud import WordCloud
from collections import Counter
import matplotlib.pyplot as plt

#df를 reveiw_df로 설정하였다
dfr = pd.read_csv('problem 1/review_df.csv')

##배달시간과 리뷰평점, 주문금액 사이의 상관관계##
correlation = dfr['rating'].corr(merged_df['order_amount', 'delivery_time'])
print(f"배달시간과 리뷰평점, 주문금액 사이의 상관관계: {correlation:.4f}")

##df category의 결측치 'etc'로 대체##
dfr['review_text'].fillna('‘No Comments', inplace=True)
#리뷰텍스트열을 지정해줬다.
review_text = dfr['review_text']
#review_text의 워드클라우드를 형성하기 위해서 상위 50개의 단어를 추출할 것이다.
#카운터함수를 불러왔다.
dfr_counts = Counter()

# 출현 빈도 카운트
result = Counter(review_text)
# 빈도 상위 50개 추출
most_word_50 = result.most_common(50)

#워드 클라우드 출력하기
plt.figure(frgsize= (5,5))
plt.imshow(result)
plt.axis('off')
plt.show()
print(most_word_50)





