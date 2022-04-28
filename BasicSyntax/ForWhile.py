# while
'''
n=0
while n<5:
    print("*",end="")
    n+=1
'''

'''
layer = input("layer:")
layer= int(layer)
i=0
while i<layer:
    print("")
    
    j=layer
    while j > i:
        print("*",end="")
        j-=1
    i+=1
'''

# for 
'''
#list = [3,4,5]  
for x in "helo":
    print(x)
'''

#"range(5)"-> [0,1,2,3,4]
# for i in range(parameter)  just like i = something   
'''
answer=0
for i in range(10+1):
    answer+=i

print(answer)
'''
# continute and break
# even addition
'''
n=0
for x in [0,1,2,3]:
    if x%2 == 0:
        continue
    n+=1
print(n)
'''

# even addition
'''
sum = 0
i=0
while i<10: # 0 can't % anynumber 
    i+=1
    if i%2==1:
        continue
    sum=sum+i
print(sum)
'''


# while 寫法
'''
i=0
while i <100 :
    i+=1

    x=0
    while x<100 :
        if x*x == i :
            print(i,"is",x,"or",-x,"square root")
        x+=1
''' 

# for 寫法
'''
for i in range(1,101):
    for j in range(11):
        if j*j == i:
            print(i)
'''


    
