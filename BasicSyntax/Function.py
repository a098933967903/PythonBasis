#function
'''
def name(x):
    print(x)

name("meow")
'''


#addition function
'''
def AddTwoNumber(num1,num2):
    answer = num1+num2
    return answer

sum=AddTwoNumber(10,20)
print(sum)
'''
# recursive
'''
n = int(input())

def factorial(x):
    if x > 1:
        return x*factorial(x-1)
    elif x==1:
        return 1

print(factorial(n))
'''

#return None
'''
def ReturnNone(x):
    
    return  # To end the function and return None

a="string"
print(ReturnNone(a))
'''

#Initial valu to Function
'''
def say(msg="Hello"):   #Set up initial values
    print(msg)

say()
'''

#Using name corespone sequence with function
'''

def divide(num1=20,num2=5):
    answer= num1/num2
    print(num1/num2)

divide()
divide(num2=20,num1=5)

'''
'''
def power(x,y=0):
    answer= x**y
    print(answer)
number,square = input("Inpute numbers:  ").split()
number = float(number)
square = float(square)
power(number,square)

'''
'''
def AvargeScore(*score):
    return
'''


def AvargeScore(*score):  # tuple 
    avarge = 0.0
    for i in score:
        avarge = avarge+i
    
    avarge=avarge/(len(score))
    print(avarge)



AvargeScore(12,23,14,54)

