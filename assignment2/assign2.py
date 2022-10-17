import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.svm import  SVC
import numpy as np
from sklearn.metrics import accuracy_score

w = datasets.load_wine()

df = pd.DataFrame(data = w.data)
df['label'] = w.target
df.info()

# plt.scatter(df[0][df["label"] == 0], df[1][df["label"] == 0],
#             color='red', marker='o', label='malignant')
# plt.scatter(df[0][df["label"] == 1], df[1][df["label"] == 1],
#             color='green', marker='*', label='benign')
# plt.xlabel('Radius')
# plt.ylabel('Texture')
# plt.legend(loc='upper left')
# plt.show()

X=df.iloc[:,0:2]
y=df['label']

svm = SVC(kernel='rbf', random_state=1, gamma=1, C=20)
svm.fit(X, y)



def plot_contours(ax, clf, xx, yy, **params):
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    out = ax.contourf(xx, yy, Z, **params)
    return out

def make_meshgrid(x, y, h=.02):
    x_min, x_max = x.min() - 1, x.max() + 1
    y_min, y_max = y.min() - 1, y.max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    return xx, yy

fig, ax = plt.subplots()

title = ('Decision surface of SVC ')

X0, X1 = X.iloc[:, 0], X.iloc[:, 1]
xx, yy = make_meshgrid(X0, X1)

plot_contours(ax, svm, xx, yy, cmap=plt.cm.YlGn, alpha=0.8)
ax.scatter(X0, X1, c=y, cmap=plt.cm.coolwarm, s=50, alpha=0.7 )
ax.set_xlabel('Radius')
ax.set_ylabel('Texture')
ax.set_xticks(())
ax.set_yticks(())
ax.set_title(title)
plt.show()

y_pred=svm.predict(X)
print(accuracy_score(y, y_pred))











# df=pd.read_csv("C:/Users/NISA/Riverdale_Episodes_IMDb_Ratings.csv",sep=';', header=None)
# # df = pd.DataFrame()
# # df["rating"] = df.target
# df.info()

# plt.scatter(df[0][df["rating"] == 0], df[1][df["rating"] == 0],
#             color='red', marker='o', label='malignant')
# plt.scatter(df[0][df["rating"] == 1], df[1][df["rating"] == 1],
#             color='green', marker='*', label='benign')
# plt.xlabel('Radius')
# plt.ylabel('Texture')
# plt.legend(loc='upper left')
# plt.show()


# # df.rename(columns = {'rating':'rating'}, inplace=True)

# # df['rating']=np.where(df['rating']>75,'good','bad')
# # df

# # X=df.iloc[:,0:2]
# # y=df['rating']

# # svm = SVC(kernel='rbf', random_state=1, gamma=0.001, C=10)

# # #train the model
# # svm.fit(X, y)