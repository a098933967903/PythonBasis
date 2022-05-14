# Analyze data


import pandas 

#to read the data and to ransport csv into dataFrame

dataTable = pandas.read_csv("googleplaystore.csv")
print(dataTable)

print("==================================================")

print("trying to get information")

print("table 大概的形狀", dataTable.shape)
print("tuble columns",dataTable.columns) 
print("==================================================")


print("Showing data that is we want to know.")

print(dataTable["Rating"])

rating = dataTable["Rating"]

print("Average of Rating", rating.mean())
print("MedianNumber of Rating", rating.median())
print("前一百名 rating 平均",rating.nlargest(100).mean())




print("===================================================")
print("找出奇怪的數值")

condictionFindOver5 = rating >5
print(dataTable[condictionFindOver5]) 


print("===================================================")
print("Exclude the odd data")

conditionExcludeOver5 = rating <=5
exData = dataTable[conditionExcludeOver5]
print(exData)



print("前一百名 rating 平均",exData["Rating"].nlargest(100).mean())

print("====================================================")
print("to Analye Install")

print(dataTable.columns)
print(dataTable["Installs"])




print("=======================================================")
print("filter the odd data ")
# We could know odd charator (+ and ,)

dataTable["Installs"] = pandas.to_numeric(dataTable["Installs"].str.replace("[+,]","").replace("Free","")) 
#print(dataTable["Installs"][10472]) # Fucking Free 



print("Average of install is ", dataTable["Installs"].mean())


over100000Condition =  dataTable["Installs"]> 100000
print("Over 100000 installed ",dataTable[over100000Condition].shape) 




print("========================================================")
print("Using keywords search the APP")

keywords = input("Enter the keywords")
conditionKeyword = dataTable["App"].str.contains(keywords,case= False) # contains(variable, ignore 大小寫)
print("The result of a searching is:", dataTable[conditionKeyword])



















