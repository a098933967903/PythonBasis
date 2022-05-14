import pandas

testColumn = pandas.Series([54,23,90])

#filter value

condition = testColumn>30
print("filterCondition",condition,sep="\n")


print("=================================================")

filterTestColumn = testColumn[condition]
print(filterTestColumn,sep="\n")


print("=================================================")

testColumn2 = pandas.Series(["智晟王者","家偉盜賊","冠霖盜賊"])


print(testColumn2)


print("===================================================")
print("display what you want to show")

stringCondition= testColumn2.str.contains("王者") #options   #stringCondition = [True,False,True,]

testColumn2 = testColumn2[stringCondition]
print(testColumn2)

print("==================================================")

studentTable = pandas.DataFrame(
    {
        "name":["智晟","家偉","冠霖","佑豪"],
        "score":[100,80,75,34,]

    }
)
print(studentTable)
print("=================================================")
print("pass > 60")

condition = studentTable["score"] >= 60           #condition = [True,False,False,True]

print(studentTable[condition])

print("==================================================")
print("取得智晟的成績")

condition = studentTable["name"] == "智晟"
print(studentTable[condition])



