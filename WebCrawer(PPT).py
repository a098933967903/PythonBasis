


# Crawler(PTT) 


import urllib.request as request    # urllib 

def getdata(url):

    # to create the request object to disguise (requestHeader)

    superRequest=request.Request(url,headers={
        "cookie":"over18=1",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    })

    with request.urlopen(superRequest) as respond:
        sourceCode = respond.read().decode("utf-8")

    #print(sourceCode)

    # to parse a resource code by using beatuifulsoup4 to get waht you want .

    import bs4
    root = bs4.BeautifulSoup(sourceCode,"html.parser") #declare what type of web was paresed. 解析HTML 語法工具
    title = root.find_all("div", class_="title")   # find_all(tag,context) 

    for title in title :
        if title.a != None:     # select tag 
            print(title.a.string)

    previosuPage = root.find("a", string="下頁 ›")

    #print(previosuPage)        # inspect
    #print(previosuPage["href"])
    return previosuPage["href"]

#url="https://www.ptt.cc/bbs/sex/index1.html"

#print("https://www.ptt.cc/"+getdata(url))

'''  Use while to simplify program
nextlink1 = "https://www.ptt.cc/"+getdata(url)
print(getdata(nextlink))

nextlink2 = "https://www.ptt.cc/"+getdata(nextlink1)
print(getdata(next2link))
'''

nextlink="https://www.ptt.cc/bbs/sex/index1.html"
Counter = 0
while Counter <20:
    nextlink = "https://www.ptt.cc/"+getdata(nextlink)   #recursive 反向
    Counter +=1



    




