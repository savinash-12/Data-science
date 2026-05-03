import numpy as np
import pandas as pd

#Importing modules
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder

df = pd.read_csv('covid_toy.csv')
# print(df.head())

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(df.drop(columns=['has_covid']),df['has_covid'],test_size=0.2)
print(x_train)


#normal way
#adding simple imputer to fever col
si = SimpleImputer()
x_train_fever = si.fit_transform(x_train[['fever']])

#also the test data
x_test_fever = si.fit_transform(x_test[['fever']])
print(x_train_fever)


#Ordinalencoding -> cough
oe = OrdinalEncoder(categories=[['Mild','Strong']])
x_train_cough = oe.fit_transform(x_train[['cough']])

#also the test data
x_test_cough = oe.fit_transform(x_test[['cough']])
print(x_train_cough.shape)

#OneHotEncoding -> gender,city
ohe = OneHotEncoder(drop='first')
x_train_gender_city = ohe.fit_transform(x_train[['gender','city']])

#also in test data
x_test_gender_city = ohe.transform(x_test[['gender','city']])
print(x_train_gender_city.shape)

#Extracting Age
x_train_age = x_train.drop(columns=['gender','fever','cough','city']).values

#also the test data
x_test_age = x_test.drop(columns=['gender','fever','cough','city']).values
print(x_train_age)


#now concatenate
# x_train_transformed = np.concatenate((x_train_age,x_train_fever,x_train_gender_city,x_train_cough), axis=1)

#also the test data
# x_test_transformed = np.concatenate((x_test_age,x_test_fever,x_test_gender_city,x_test_cough), axis=1)
# print(x_train_transformed.shape)


#now quick and efficient way
from sklearn.compose import ColumnTransformer
transformer = ColumnTransformer(transformers=[
    ('tf1',SimpleImputer(),['fever']),
    ('tf2',OrdinalEncoder(categories=[['Mild','Strong']]),['cough']),
    ('tf3',OneHotEncoder(drop='first'),['gender','city']),
],remainder='passthrough')

print(transformer.fit_transform(x_train).shape)
print(transformer.fit_transform(x_test))