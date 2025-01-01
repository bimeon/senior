import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import f1_score,accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import svm, tree, metrics
import warnings
# 경고창 숨기기
warnings.filterwarnings('ignore')

# csv 파일 불러오기
loan_data = pd.read_csv('loan_data_final.csv')

#####문제 1 #####
loan_data_numeric=loan_data[['credit_score','monthly_income','debt_ratio','loan_amount','repaid']]
#기초 통계량 확인하기
print(loan_data_numeric.info())
print(loan_data_numeric.describe())

fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (25, 10))

#월 소득과 부채 비율의 관계 산점도 그리기
data_correlation_1=loan_data[['monthly_income','debt_ratio','repaid']]
# 대출 상환 여부 색상으로 구분하기 위한 변수 저장
grouped_repaid=data_correlation_1.groupby('repaid')
# 대출 상환 여부 기준으로 구분하기 위한 for문 사용
for i, items in grouped_repaid:
    ax1.scatter('monthly_income','debt_ratio',data=items,label=i)# 산점도 그리기
    ax1.set_title("Monthly Income vs Debt Ratio")# 그래프 제목 지정
    ax1.set_xlabel("monthly_income")# X값 제목 지정
    ax1.set_ylabel("debt_ratio")# Y값 제목 지정
    ax1.legend(loc='upper right',title='repaid')

#신용 점수와 대출 금액의 관계 산점도 그리기
data_correlation_2=loan_data[['credit_score','loan_amount','repaid']]
# 대출 상환 여부 색상으로 그룹을 나누기 위한 변수 저장
grouped_repaid=data_correlation_2.groupby('repaid')
# 대출 상환 여부 기준으로 그룹을 나누기 위한 for문 사용
for i, items in grouped_repaid:
    ax2.scatter('credit_score','loan_amount',data=items,label=i)# 산점도 그리기
    ax2.set_title("Credit Score vs Loan Amount")# 그래프 제목 지정
    ax2.set_xlabel("credit_score")# X값 제목 지정
    ax2.set_ylabel("loan_amount")# Y값 제목 지정
    ax2.legend(loc='upper right',title='repaid')

plt.show()


#####문제 2 #####

#성과지표 수집을 위해 decisiontree성능 리스트와 svm성능 리스트를 선언한다
dt_f1score=[]
dt_accuracy=[]
svm_accuracy = []
svm_f1score = []

#X값과 y값을 컬럼을 기준으로 분리해준다
X=loan_data[['credit_score','monthly_income','debt_ratio','loan_amount']]
#타겟값 y로 지정
y=loan_data[['repaid']]

###DecisionTree모델###

for _ in range(100):#학습 100번 반복
    # 훈련 데이터와 테스트 데이터를 8:2로 분리해준다
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    dt_model = DecisionTreeClassifier(max_depth=2)# DecisionTree모델
    dt_model.fit(X_train, y_train)# 훈련용 데이터로 학습시킨다
    y_pred_dt = dt_model.predict(X_test) #테스트 데이터로 예측시킨다
    dt_f1score.append(f1_score(y_test,y_pred_dt))#f1score값 리스트에 추가
    dt_accuracy.append(accuracy_score(y_test,y_pred_dt))#accuracy 리스트에 추가

###SVM모델###

C = 2 # SVM의 regularization parameter

for i in range(100):# 학습 100번 반복
    # 훈련 데이터와 테스트 데이터를 8:2로 분리해준다
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    clf = svm.LinearSVC(C=C)  # svm모델
    clf.fit(X_train, y_train)# 훈련용 데이터로 학습시킨다
    y_pred_svm = clf.predict(X_test) #테스트 데이터로 예측시킨다
    svm_accuracy.append(metrics.accuracy_score(y_test, y_pred_svm)) #accuracy 리스트에 추가
    svm_f1score.append(metrics.f1_score(y_test, y_pred_svm)) #f1score값 리스트에 추가

###성능 출력을 위한 데이터프레임 변환 및 통계값 출력###

# DecisionTree 모델 성능을 담은 리스트를 데이터프레임으로 변환하는 과정
DecisionTree_performance=pd.DataFrame({'accuracy':dt_accuracy,'f1_score':dt_f1score})
#성능에 대한 통계값을 출력하도록 한다
print("Decision Tree Performance : ")
print(DecisionTree_performance.describe())

# SVM모델 성능을 담은 리스트를 데이터프레임으로 변환하는 과정
svm_performance=pd.DataFrame({'accuracy':svm_accuracy,'f1_score':svm_f1score})
#성능에 대한 통계값을 출력하도록 한다
print("SVM Performance : ")
print(round(svm_performance.describe(),6))
