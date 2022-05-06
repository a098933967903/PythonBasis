'''
file = open("text.txt",mode="w",encoding="utf-8")
file.write("Meow\n駭客")
file.close
'''


'''
with open("text.txt",mode="w",encoding="utf-8") as file:
    file.write("MeowHecker")
'''


'''
with open("text.txt",mode="w",encoding="utf-8") as file:
    file.write("2\n5\n7\n3")


with open("text.txt",mode="r") as file:
    sum=0
    for numbers in file:
        sum=sum+int(numbers)
    print(sum)
'''

import json

#to write config.json
with open("config.jason",mode="w" ) as config:
    config.write(str({"Host":"windows","version":"1.9.3"}))  #write("str") ->use str() to casting

# to read json file and print
with open("config.json",mode="r",encoding="utf-8") as config:
    data = json.load(config)
print(data)
print(data["Host"]) #dictionary
print(data["version"])

# to fix json file
data["Host"] = "linux"  #to fix that data was read 

with open("config.json",mode="w") as config:
    #Rrcover file
    json.dump(data,config) 

print(data)
    
    







