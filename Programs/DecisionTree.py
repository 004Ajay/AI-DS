from sklearn import tree
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt # to show D-Tree graph

data = load_breast_cancer()
X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, 
                            test_size=0.3, random_state=1)
clf = tree.DecisionTreeClassifier().fit(X_train, y_train)
pred = clf.predict(X_test)

plt.figure(figsize=(15, 15)) # Resize figure
tree.plot_tree(clf, filled=True)
plt.show()

print(f"Accuracy: {round(accuracy_score(pred, y_test)*100, 2)}%")