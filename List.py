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
