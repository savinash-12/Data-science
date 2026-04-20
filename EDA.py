import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('Titanic-Dataset.csv')
from ydata_profiling import ProfileReport
prof = ProfileReport(df)
prof.to_file(output_file='output.html')
print(df.head())

# to plot a number of count in bar graph
sns.countplot(x='Sex', data=df)

# to plot a number of count in pie chart
df['Survived'].value_counts().plot(kind='pie',autopct='%1.1f%%')
plt.show()

# hist graph plot
plt.hist(df['Age'],bins=10)

# distplot
sns.distplot(df['Age'])
plt.show()

# box plot
plt.boxplot(df['Fare'])
plt.show()

print(df.describe())
# skew(normal symmetricity)