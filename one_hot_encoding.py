import numpy as np
import pandas as pd

# print("hello")


df = pd.read_csv('cars.csv')
# print(df.head())

# print(df['owner'].value_counts())

#OneHotEncoding using Pandas
# print(pd.get_dummies(df, columns=['fuel','owner']))

#K-1 encoding
# print(pd.get_dummies(df, columns=['fuel','owner'],drop_first=True))

#OneHotEncoding using Sklearn
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(df.iloc[:,0:4],df.iloc[:,-1], test_size=0.2,random_state=42)

# print(X_train.head())
# print(X_test.head())

from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(drop = 'first')
x_train_new = ohe.fit_transform(X_train[['fuel','owner']]).toarray()
x_test_new = ohe.transform(X_test[['fuel','owner']]).toarray()
print(x_test_new)

print(np.hstack((X_train[['brand','km_driven']].values,x_train_new)).shape)

#OneHoEncoding with Top Categories
counts = (df['brand'].value_counts())
print(df['brand'].nunique())
threshold = 100
repl = counts[counts <= threshold].index

print(pd.get_dummies(df['brand']).replace(repl, 'uncommon'))

