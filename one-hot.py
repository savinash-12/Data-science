import pandas as pd
# data = {'color':['Red','Blue','Green','Blue']}
# df = pd.DataFrame(data)
# df_encoded = pd.get_dummies(df,columns=['color'],prefix='color')
# print(df_encoded)



#Binning
# data = {'Age': [23, 45, 18, 34, 67, 50, 21]}
# df = pd.DataFrame(data)

# bins = [0, 20, 40, 60, 100]
# labels = ['0-20', '21-40', '41-60', '61+']

# df['Age_Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

# print(df)

#Text Data Preprocessing
# import nltk
# from nltk.corpus import stopwords
# from nltk.stem import PorterStemmer
# from sklearn.feature_extraction.text import CountVectorizer

# texts = ["This is a sample sentence.", "Text data preprocessing is important."]

# stop_words = set(stopwords.words('english'))
# stemmer = PorterStemmer()
# vectorizer = CountVectorizer()


# def preprocess_text(text):
#     words = text.split()
#     words = [stemmer.stem(word)
#              for word in words if word.lower() not in stop_words]
#     return " ".join(words)


# cleaned_texts = [preprocess_text(text) for text in texts]

# X = vectorizer.fit_transform(cleaned_texts)

# print("Cleaned Texts:", cleaned_texts)
# print("Vectorized Text:", X.toarray())


#Feature Splitting

import pandas as pd

data = {'Full_Address': [
    '123 Elm St, Springfield, 12345', '456 Oak Rd, Shelbyville, 67890']}
df = pd.DataFrame(data)

df[['Street', 'City', 'Zipcode']] = df['Full_Address'].str.extract(
    r'([0-9]+\s[\w\s]+),\s([\w\s]+),\s(\d+)')

print(df)