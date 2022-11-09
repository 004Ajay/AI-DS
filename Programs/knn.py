from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
# Loading data
irisData = load_iris()
 
# Create feature and target arrays
X = irisData.data
y = irisData.target

# Split into training and test set
X_train, X_test, y_train, y_test = train_test_split(
             X, y, test_size = 0.2, random_state=42)


a=int(input("Enter the number for k value:")  )
knn = KNeighborsClassifier(n_neighbors=a)
print("Number of datas for Preiction is:",len(X_test))

knn.fit(X_train, y_train)
print("Prediction Accuracy:",knn.score(X_test, y_test)*100)
# Predict on dataset which model has not seen before
x=knn.predict(X_test)
plt.ylabel("PREDICTION")
plt.xlabel("Sl No")
plt.plot(x)
print("Predicted:",knn.predict(X_test))