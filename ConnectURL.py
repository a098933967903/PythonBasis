# urllib.request get web data

'''
import urllib.request as request

src ="https://www.ntu.edu.tw/"

#to get the data from the target
with request.urlopen(src) as response:
    data = response.read().decode("utf-8")     # get the target SourseCode , responce.read().decode("utf-8") 
print(data)
'''


'''
import urllib.request as request
import json

src="https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"

with request.urlopen(src) as response:
    data = json.load(response)

print(data)
'''

# put data into the file

import urllib.request as request
import json

src="https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"


with request.urlopen(src) as response:
    data =json.load(response)


with open("company.txt","w",encoding="utf-8") as file:  # data write into the file.txt
    CatchList=data["result"]["results"]  #分析 json key->value 
    for company in CatchList:
        print(company["公司名稱"])
        file.write(company["公司名稱"]+"\n")


#with open("data.txt","w",encoding="utf-8") as file: