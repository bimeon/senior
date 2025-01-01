from sklearn import datasets
import math
import random

wine = datasets.load_wine()
(r, c) = wine.data.shape
X = wine.data
y = wine.target

# random split 1
tr_ratio = 0.8
tr_idx = random.sample(range(r), int(math.floor(r*tr_ratio)))
te_idx = [x for x in range(r) if x not in tr_idx]

print(tr_idx, te_idx)

X_tr, y_tr, X_te, y_te = X[tr_idx, :], y[tr_idx], X[te_idx, :], y[te_idx]

# random split 2
from sklearn.model_selection import train_test_split

X_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# k-fold
from sklearn.model_selection import KFold

kf = KFold(n_splits=10)

for train_idx, test_idx in kf.split(X):
    X_train, X_test, y_train, y_test = X[train_idx], X[test_idx], y[train_idx], y[test_idx]
    print(train_idx, test_idx)