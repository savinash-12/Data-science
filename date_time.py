import pandas as pd
import numpy as np
import datetime

today = datetime.date.today()
print(today)

date = pd.read_csv("orders.csv")
time = pd.read_csv("messages.csv")

print(date.info())
print(date.head())

#converting datetime data type
date["date"] = pd.to_datetime(date["date"])
print(date.head())
print(date.info())

#Extracting the year
date["date_year"] = date["date"].dt.year
print(date.head())

#Extracting the month
date["date_month"] = date["date"].dt.month
print(date.head())

#Extracting the month name
date["month_name"] = date["date"].dt.month_name()
print(date.head())

#Extracting the days
date["date_day"] = date["date"].dt.day
print(date.head())


#day of the week
date["day_of_week"] = date["date"].dt.day_name()
print(date.head())

#day is weekend or not
date["Weekend_or not"] = np.where(date["day_of_week"].isin(['Sunday','Saturday']), 1, 0)
print(date.head())

#Extract the week of the year
# date["date_week"] = date["date"].dt.week
# print(date.head())

#Extract the quater
date["quater"] = date["date"].dt.quarter
print(date.head())

#Semester
date["semester"] = np.where(date['quater'].isin([1,2]), 1, 2)
print(date.head())