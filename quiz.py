#1

import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.svm import  SVC
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScale
# import seaborn as sns


#2
df = pd.read_csv('C:/Users/NISA/Downloads/Heart.csv', index_col = 0) #3


#4
# print(df.info())

#5
# print(df.head())

#6
# print(df.tail())

#7
# print(df.count())
# print(df.max())
# print(df.min())
# print(df.mean())
# print(df.sd())

#8
# print(df.isnull())

#9
# print(df.dropna())


#10
# corr = df.corr()
# f, ax = plt.subplots(figsize=(12, 10))
# mask = np.triu(np.ones_like(corr, dtype=bool))
# cmap = sns.diverging_palette(230, 20, as_cmap=True)
# sns.heatmap(corr, annot=True, mask = mask, cmap=cmap)

#11
# variances = df.var()
# print(variances)

#12
# def age_group(df):
#     df["Age"] = pd.cut(df["Age"], bins = [0,39,55,100], labels = ["young", "middle_aged", "elderly"])
#     return df

# print(age_group(df))


#16
# df["ChestPain"] = df["ChestPain"].astype(int)
# df["Thal"] = df["Thal"].astype(int)
# df["AHD"] = df["AHD"].astype(int)

# df.info()


#17
# print(df.corr())

#18
# scaler = StandardScaler()
# model = scaler.fit(df)
# scaled_data = model.transform(df)

# # print(scaled_data)

#19






