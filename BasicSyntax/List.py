
'''
score = [90,80,76,46,34]
score[2] = 60
print(score)

score[1:4] = [] ## 1 <= x < 4
print(score)

score = score + [50,80]
print(score)
print(len(score))  # If you want to print the list length -> use len( <variable> ) 

Nestlist = [[2,"meow",7],[2,5,9]] 
print(Nestlist[0][1]) 

Nestlist[0][0:3] = ["Meow","Meow","Meow","Meow"] # replace index of 0,1,2 and add index 3 into the list.
print(Nestlist)
'''
''' didn't work
ScoreNumbers = int(input("How many numbers do you want to input")) #Casting

ScoreList = []
i=1
while i == 1:
    if(ScoreList.append(input())!="quite"):
        ScoreList.append(input("input scores"))
    else:
        i=0
'''


# append()
'''
list=[]
list.append(input('score'))
print(list[0:]) # print all 
'''

# insert
'''
FruitList=["apples",'bananas','oranges']
FruitList.insert(2,"strawberrys")
print(FruitList)
'''