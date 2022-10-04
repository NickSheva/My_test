from sklearn import tree
import numpy as np
X = np.array([[9, 8, 2, "Computer scince"], [1, 7, 3, "Foreing languages"], [3, 5, 7, "Art"]])
Tree = tree.DecisionTreeClassifier().fit(X[:,:-1], X[:, -1])
student_0 = Tree.predict([[3, 8, 7]])
print(student_0)