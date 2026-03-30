Data Gathering
CSV
#importing pandas
import pandas as pd

#opening a local csv file
df = pd.read_csv(“Hello.csv”)

#opening a csv file from an URL

#Sep Parameter
pd.read_csv(“file_name”,sep =’\t’,names = [‘sno’,’name’])
[names is used to give the column name manually]

#Index_col Parameter
pd.read_csv(“file_name”,index_col = ‘employe_id’)
[index_col is used to make one column as indexed column]

#Header parameter
pd.read_csv(“file_name”, header = 1)
[header is used to give 1st row as the column name]

#use_cols parameter
pd.read_csv(‘file_name’, usecols = [‘abc’,’rst’])
[Used to select the particular column]

#squeeze( )
[Used to convert a single column DataFrame into a Series]

#Skiprows/nrows Parameter
pd.read_csv(“file_name”, skiprows = [0,1]) or nrows =100 [ only 100 rows will be displayed]
You can use the lambda function also.

#Encoding Parameter
pd.read_csv(“file_name”, encoding = ‘latin-1’)
[UnicodeDecoderError]

#Skip bad lines
pd.read_csv(‘file_name’, sep =’;’, encoding = ‘latin-1’, error_bad_lines = False)
[Used to skip missing values]

#dtypes parameter
pd.read_csv(‘file_name’, dtype = {‘Column_name’: int(data_type)})
[Used to convert the data types]

#Handling Dates
pd.read_csv(‘file_name’, parse_dates = [‘date’])

#Convertors
def  rename(name):
       if name == “Royal Challengers Banglore”:
                 return “RCB”
        else:
                 return name
Function call:
rename(“Royal Challengers Banglore”)

pd.read_csv(‘file_name’, converters = {‘column_name’: rename})

#na_values parameter
na_values = [‘Coulumn_name”]
[fillup all the null values]

#Loading a huge dataset in chunks
dfs = pd.read_csv(‘file_name’, chunksize = 5000)

for chunks in dfs:
      print(chunk.shape)
