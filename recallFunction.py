# Recall function 


def f(x):
    return 2*x+3


def g(x):
    return x


answer = f(g(5))

print(answer)
print("===============================")


def normalFunction(x):
    return 2*x+3
    
def callBackFunction(x):
    return x

answer= normalFunction(callBackFunction(10))

print(answer)

print("================================")
def f(x):
    return recallFunction(x)

def recallFunction(x):
    return x

answer = f(recallFunction(10))

print(answer)
print("==================================")

def f1(f2):
    f2() # call recall fucnction


def f2():
    print(100)

f1(f2)

print("================================")

def f1(f2):
    f2(100)

def f2(num):
    print(num)

f1(f2)
print("==================================")

def add(a,b,showfunction):
    showfunction(a+b)

def display(result):
    print("result is ", result)

add(10,5,display)



















    