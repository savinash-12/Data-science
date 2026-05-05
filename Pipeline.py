import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline,make_pipeline
from sklearn.feature_selection import SelectKBest,chi2
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv('Titanic-Dataset.csv')
print(df.head())

df.drop(columns=['PassengerId','Name','Ticket','Cabin'],inplace=True)

#step 1 train/test/split
x_tain,x_test,y_train,y_test = train_test_split(df.drop(columns =['Survived']),df['Survived'],test_size=0.2,random_state=42)
print(x_tain.head())

# imputation transformer

trf1 = ColumnTransformer([
    ('impute_age',SimpleImputer(),[2]),
    ('impute_embarked',SimpleImputer(strategy='most_frequent'),[6])
],remainder = 'passthrough')

# one hot encoding
trf2 = ColumnTransformer([
    ('Ohe_sex_embarked',OneHotEncoder(handle_unknown='ignore',sparse_output=False),[1,6]),
],remainder = 'passthrough')

#scaling
trf3 = ColumnTransformer([
    ('scale',MinMaxScaler(),slice(0,10)),
])

#Feature selection
trf4 = SelectKBest(score_func=chi2,k=8)

#train the model
trf5 = DecisionTreeClassifier()

#create a Pipeling
pipe = Pipeline([
    ('trf1',trf1),
    ('trf2',trf2),
    ('trf3',trf3),
    ('trf4',trf4),
    ('trf5',trf5)
])

#alternate syntax for pipeline
# pipe = make_pipeline(trf1,trf2,trf3,trf4,trf5)

#train
pipe.fit(x_tain,y_train)

#can see the content
print(pipe.named_steps)
print(pipe.named_steps['trf1'].transformers_[0][1].statistics_)
print(pipe.named_steps['trf1'].transformers_[1][1].statistics_)

#Display Pipeline
from sklearn import set_config
set_config(display='diagram')
#
# #fix display problem
from sklearn.utils import estimator_html_repr

html = estimator_html_repr(pipe)

with open("pipeline.html", "w", encoding="utf-8") as f:
    f.write(html)

# import webbrowser
webbrowser.open("pipeline.html")

#Predict
y_pred = pipe.predict(x_test)
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test,y_pred)
print(accuracy)
print(y_pred)


#Cross validation using Pipeline
#cross validation using cross_val_score

from sklearn.model_selection import cross_val_score
print(cross_val_score(pipe,x_tain,y_train,cv=5,scoring='accuracy').mean())

#GridSearch using pipeline
params = {
    'trf5__max_depth':[1,2,3,4,5,None]
}

from sklearn.model_selection import GridSearchCV
grid = GridSearchCV(pipe,params,cv=5,scoring='accuracy')
gird = grid.fit(x_tain,y_train)
print(grid.best_score_)
print(grid.best_params_)

#Exporting the Pipeline
#export
import pickle
pickle.dump(pipe,open('pipe.pkl','wb'))