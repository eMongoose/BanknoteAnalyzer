# import libraries
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_validate
from loadfile import load_data
import numpy as np

def KNNmodel():
    X, y = load_data("./Dataset/data_banknote_authentication.csv")

    score_accuracy = []
    score_precision = []

    # test k = {1, 2, ..., 10}
    k_array = [i for i in range(1, 11, 1)]
    for k in k_array:
        knn = KNeighborsClassifier(n_neighbors = k) 
        scores = cross_validate(knn, X, y, cv=10, scoring=("accuracy", "precision"))
        
        #print(scores)
        score_accuracy.append(np.mean(scores["test_accuracy"]))

    print("Accuracy:\n")
    print(score_accuracy)

