'''
class girl:
    girlName=["星星","奈奈"]

    def read(Girl):
        if Girl not in girl.girlName:
            print("not support it")
        else:
            print("success")

girl.read("星星")
girl.read("每每")
'''
# instant 

'''


class Point:
    # create instant

    def __init__(self,x,y):
        self.x = x 
        self.y = y

p1 = Point(3,4)

p2= Point(1,0)

print(p1.x,p1.y)
print(p2.x,p2.y)
'''

'''

class FullName:
    def __init__(self,frist,last):
        self.frist=frist
        self.last=last
        
Master = FullName("侯","帥晟")
print(Master.frist,Master.last)

slaver = FullName("X","XX")
print(slaver.frist,slaver.last)

'''

# install + 

