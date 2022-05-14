from itertools import product


def yieldNumber():  #through forloop to yield 
    print("frist phase")
    yield 3
    yield 5
    yield 10


generator = yieldNumber()
print(generator)   # we could know this time function only load generator (not number)

for x in generator:
    print(x)