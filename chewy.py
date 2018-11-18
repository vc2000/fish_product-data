from bs4 import BeautifulSoup
import pandas
import requests

base_url = "https://www.chewy.com/s?rh=c%3A885"
big_lis=list()
for num in range(0,26):
    if num == 0:
        r=requests.get(base_url)
    else:
        r=requests.get(base_url+ "&page=" + str(num))


    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    all=soup.find_all("div",{"class":"content"})

    for items in all:
        d={}
        d["brand"] = items.find("h2").find("strong").text
        d["title"] = items.find("h2").find("strong").next_sibling.replace("\n","").replace("\t","")
        information = items.find("div",{"class":"product-info"})
        for info in information:
            try:
                d["auto_reorder_price"]=items.find("p",{"class":"autoship"}).find("strong").text.replace("\n","").replace("\t","").replace("$","")
            except:
                print(None)
            try:
                d["price"]=item s.find("p",{"class":"price"}).find("strong").text.replace("\n","").replace("\t","").replace("$","")
            except:
                print(None)


        big_lis.append(d)

"""count=1
for i in big_lis:
    print(count)
    print(i)
    count +=1"""
df=pandas.DataFrame(big_lis)
df.to_csv("chewy.csv")
