from functools import total_ordering
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
        "salary":[9921319,23213421,99999],
        "age":[20,40,23]
    }, index=range(3)  #set up table index
)
print(Dim2Data)

print("=======================================")
#basis information 
'''
print(Dim2Data.iloc[2])    #iloc=I location -＞　using list show the row  , sequence 
print("data_type"+"(rows,columns)",Dim2Data.shape)
print("data index",Dim2Data.index)

print("======================================")

print(Dim2Data.loc["c"],sep="\n") # lic -> indext
print("get column\n", Dim2Data['salary'])
'''
# calculate average of salary

'''
columnSalary = Dim2Data["salary"]
total = columnSalary[0]+columnSalary[1]
print(total)
print(columnSalary.mean()) # mean get average
'''
# to create new column

Dim2Data["rank"] = pandas.Series([3,2,1])  #　正式寫法
Dim2Data["revenue"] = [123214,25343453,3342342352]

Dim2Data["cp"]=Dim2Data["revenue"]/Dim2Data["salary"]



print(Dim2Data)






