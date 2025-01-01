import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#csv 파일 불러오기
loan_data_final = pd.read_csv('loan_data_final.csv')

### 1번

#고객 데이터 탐색
print(loan_data_final.info())

#고객 데이터의 각 변수의 기본 통계량(평균, 분산 등) 확인
print(loan_data_final.describe())

#monthly_income(월 소득)과 debt_ratio(부채 비율)의 관계 산점도 그리기
sns.scatterplot(data=loan_data_final, x='monthly_income', y='debt_ratio',hue = "repaid", markers='o', alpha=0.6)
# 산점도 그래프 제목 설정
plt.title('Monthly Income vs Debt Ratio')
#산점도 그래프 시각화
plt.show()

##credit_score(신용 점수)와 loan_amount(대출 금액)의 관계 산점도 그리기
#fig size 조정
plt.figure(figsize=(10, 6))
#관계 산점도 설정
sns.scatterplot(data=loan_data_final, x='credit_score', y='loan_amount',hue = "repaid", markers='o', color='grey', alpha=0.6)
#산점도 제목 지정
plt.title('Credit Score vs Loan Amount')
#산점도 그리기
plt.show()

### 2번

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn import svm, tree
from sklearn.metrics import accuracy_score, f1_score, classification_report

X = loan_data_final[['credit_score','monthly_income','debt_ratio','loan_amount']]# 데이터셋의 특징값
y = loan_data_final['repaid'] # 데이터셋의 레이블

#데이터를 학습세트(80%)와 테스트 세트(20%)으로 분리
X_tr, X_te, y_tr, y_te = train_test_split(X,y,test_size = 0.2)

# ##각 모델의 실험을 100회 반복
# epochs = 100
# for epoch_index in range(epochs):

#선형 커널(linear kernel)을 사용하는 Support Vector Machine 분류 모델을 생성합니다.
#SVM 모델 학습 및 평가
trained_svm = svm.SVC(kernel = 'linear').fit(X_tr, y_tr)
y_pred = trained_svm.predict(X_te)

#DT 모델 학습 및 교차검증
dt_model = tree.DecisionTreeClassifier()
cv_scores = cross_val_score(dt_model, X, y, cv=10)

# Decision Tree 성능 출력(정확도, F1-SCORE)
print("Decision Tree performance: ")
#print(classification_report(y, cv_scores))
print("Accuracy", cv_scores.mean())
print("f1_score", cv_scores)

# SVM 성능 출력(정확도, F1-SCORE)
print("SVM performance :")
print(classification_report(y_te, y_pred))
print("SVM Accuracy", accuracy_score(y_te, y_pred))
print("f1_score",f1_score(y_te, y_pred) )