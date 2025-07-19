from sklearn.linear_model import SGDClassifier
from picklemodel import load_model

def lc_predict(X):
  model = load_model('lc')
  prediction = model.predict(X)

  return prediction