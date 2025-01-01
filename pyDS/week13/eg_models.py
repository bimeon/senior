from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn import svm, tree
from sklearn.metrics import accuracy_score, confusion_matrix

wine = load_wine()
X = wine.data
y = wine.target

X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2)

trained_svm = svm.SVC(kernel='linear').fit(X_tr, y_tr)
y_pred = trained_svm.predict(X_te)

print(confusion_matrix(y_te, y_pred))
print(accuracy_score(y_te, y_pred))

dt_clf = tree.DecisionTreeClassifier()
acc_dt = cross_val_score(dt_clf, X, y, cv=10)

print(acc_dt)
print(acc_dt.mean())