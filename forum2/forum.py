from sklearn import datasets
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics

wine = datasets.load_wine()

# print("Features:", wine.feature_names)
# print("Labels:", wine.target_names)

# print(wine.data.shape)

# print(wine.data[0:5])

# print(wine.target)

X_train, X_test, y_train, y_test = train_test_split(wine.data, wine.target, test_size=0.3,random_state=200)
clsfy = svm.SVC(kernel = 'linear')
clsfy.fit(X_train, y_train)

#testset
y_pred = clsfy.predict(X_test)
print("Test Accuracy score:", metrics.accuracy_score(y_test, y_pred))

#trainset
y_pred2=clsfy.predict(X_train)
print("Train Accuracy score:", metrics.accuracy_score(y_train, y_pred2))

# Test Accuracy score: 0.9629629629629629
# Train Accuracy score: 0.9838709677419355



