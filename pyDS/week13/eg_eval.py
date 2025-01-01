from sklearn import metrics
from sklearn.metrics import confusion_matrix

y_te = [1, 0, 1, 1, 0]
pred = [1, 1, 1, 1, 1]

print(confusion_matrix(y_te, pred))
print(metrics.accuracy_score(y_te, pred))
print(metrics.recall_score(y_te, pred))
print(metrics.precision_score(y_te, pred))
print(metrics.f1_score(y_te, pred))
