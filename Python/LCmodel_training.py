from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import cross_validate
from loadfile import load_data
from picklemodel import store_model
import numpy as np

# import matplotlib.pyplot as plt

X, y = load_data("./Dataset/data_banknote_authentication.csv")

lc = SGDClassifier(loss='log_loss')
lc.fit(X, y)
#scores = cross_validate(clf, X, y, cv=10)
# print(scores)

# test prediction against known results
print(lc.predict([[3.6216,8.6661,-2.8073,-0.44699]]))
print(lc.predict([[-4.8554,-5.9037,10.9818,-0.82199]]))

store_model('lc', lc)

# print(clf.coef_, clf.intercept_)

# plt.scatter(X['variance'], X['skewness'])
#plt.show()
#plt.close()