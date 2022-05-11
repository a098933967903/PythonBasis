from statistics import median
import pandas    # Usually, we will set pandas as pd 
'''
# create column


column = pandas.Series([12,32,43,12]) 
print(column)

print("Max",column.max())
print("min",column .min())
print("media",column.median())

column*=2     #the column multiple 2 
print(column)


# 
column=column==24
print(column)
'''

#Dataframe (it's mean that it's 2 dimension 

Dim2Data=pandas.DataFrame(
    {
        "name":["jacky","mandy","meowhecker"],
        "salary":[999999999,12,9999999999999999999999999999],
        "age":[20,40,23]
    }
)
print(Dim2Data)

print("=======================================")

print(Dim2Data.iloc[2])


