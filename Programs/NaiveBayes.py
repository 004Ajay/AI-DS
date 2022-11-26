from sklearn import datasets
iris = datasets.load_iris()
x, y = iris.data, iris.target

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=123)

from sklearn.naive_bayes import GaussianNB
NB = GaussianNB().fit(x_train, y_train)
pred = NB.predict(x_test)

from sklearn.metrics import confusion_matrix, classification_report
print("Confusion Matrix:\n", confusion_matrix(y_test, pred))
print("\nReport:\n", classification_report(y_test, pred))


"""
# Metrics in one by one format 
from sklearn.metrics import make_scorer, accuracy_score,precision_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score ,precision_score,recall_score,f1_score

cm = confusion_matrix(y_test, pred)
accuracy = accuracy_score(y_test,pred)
precision =precision_score(y_test, pred, average='micro')
recall =  recall_score(y_test, pred, average='micro')
f1 = f1_score(y_test, pred, average='micro')
print('Confusion matrix for Naive Bayes\n',cm)
print('accuracy: ' , round(accuracy*100, 2))
print('precision:', round(precision*100, 2))
print('recall:' ,round(recall*100, 2))
"""