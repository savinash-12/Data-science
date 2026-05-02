import numpy as np #linear algebra
import pandas as pd # data processing
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('wine_data.csv',header=None,usecols=[0,1,2])
df.columns = ['Class label','Alcohol', 'Malic acid']

# print(df.head())
# print(df)
# kdeplot
# sns.kdeplot(df['Alcohol'])
# sns.kdeplot(df['Malic acid'])
# plt.show()

#scatter plot some error in this code
# color_dict = {1:'red',3:'green',2:'blue'}
# sns.scatterplot(df['Alcohol'],df['Malic acid'],hue = df['Class label'],palette=color_dict)
# plt.show()

# scatter plot
# color_dict = {1: 'red', 3: 'green', 2: 'blue'}
#
# sns.scatterplot(
#     x=df['Alcohol'],
#     y=df['Malic acid'],
#     hue=df['Class label'],
#     palette=color_dict
# )
#
# plt.show()

from sklearn.model_selection import train_test_split
x_train, x_test,y_train,y_test = train_test_split(df.drop('Class label', axis = 1), df['Class label'], test_size = 0.3, random_state = 0)
print(x_train.shape)
print(x_test.shape)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
#fit the scaler to the train set, it will learn tha parameters
scaler.fit(x_train)
#transform train and test sets

x_train_scaled = scaler.transform(x_train)
x_test_scaled = scaler.transform(x_test)

x_test_scaled = pd.DataFrame(x_test_scaled, columns = x_test.columns)
x_train_scaled = pd.DataFrame(x_train_scaled, columns = x_train.columns)
# print(np.round(x_train.describe(), 1))
# print(np.round(x_train_scaled.describe(), 1))

#before and after processing
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 5))

ax1.scatter(x_train['Alcohol'], x_train['Malic acid'],c=y_train)
ax1.set_title("Before Scaling")
ax2.scatter(x_train_scaled['Alcohol'], x_train_scaled['Malic acid'],c=y_train)
ax2.set_title("After Scaling")
plt.show()

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 5))

# before scaling
ax1.set_title('Before Scaling')
sns.kdeplot(x_train['Alcohol'], ax=ax1)
sns.kdeplot(x_train['Malic acid'], ax=ax1)

# after scaling
ax2.set_title('After Standard Scaling')
sns.kdeplot(x_train_scaled['Alcohol'], ax=ax2)
sns.kdeplot(x_train_scaled['Malic acid'], ax=ax2)
plt.show()

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 5))

# before scaling
ax1.set_title('Alcohol Distribution Before Scaling')
sns.kdeplot(x_train['Alcohol'], ax=ax1)

# after scaling
ax2.set_title('Alcohol Distribution After Standard Scaling')
sns.kdeplot(x_train_scaled['Alcohol'], ax=ax2)
plt.show()

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 5))

# before scaling
ax1.set_title('Malic acid Distribution Before Scaling')
sns.kdeplot(x_train['Malic acid'], ax=ax1)

# after scaling
ax2.set_title('Malic acid Distribution After Standard Scaling')
sns.kdeplot(x_train_scaled['Malic acid'], ax=ax2)
plt.show()