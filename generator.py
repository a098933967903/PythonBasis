

import numbers
from typing import Counter


def yieldNumber():  #through forloop to yield 
    print("frist phase")
    yield 3
    yield 5
    yield 10


generator = yieldNumber()
print(generator)   # we could know this time function only load generator (not number)

for x in generator:
    print(x)


print("===========================================")


def genetatorSingular(Maxumber):
    '''
    number = 1    #if variable write in outside, it wouldn't be executed 
    yield number
    number+=2   
    yield number
    number+=2
    yield number
    '''
    number = 1
    while number < Maxumber:
        yield number
        number+=2
        





singularNumber = genetatorSingular(100)

for data in singularNumber:
    print(data)