from bs4 import BeautifulSoup
import pandas
import requests

base_url = "https://www.petmountain.com/category/aquarium"
r=requests.get(base_url)
c=r.content
soup=BeautifulSoup(c,"html.parser")
categories_div=soup.find("div",{"class":"category-filters col-lg-3"})

diff_category = ["aquarium-chillers","aquarium-fish-feeders","aquarium-powerheads","aquarium-power-strips-timers",
"aquarium-skimmers","aquarium-thermometers","aquarium-water-pumps","aquarium-water-tubing","organic-aquarium-supplies"]

for category_url in categories_div.find_all('a', href=True):
    big_lis =[]
    file_name= category_url['href'][46:]

    r=requests.get(category_url['href'])
    c=r.content
    soup=BeautifulSoup(c,"html.parser")

    for i in diff_category:
        if i in file_name:
            print ("diff :" + file_name)

            product_info= soup.find_all("div",{"class":"col-6 col-md-4 mb-5"})
            for info in product_info:
                print(count)
                d={}
                d["brand"] = info.find("span",{"class":"brand"}).text
                d["title"] = info.find("span",{"class":"product-name"}).text
                d["price"] = info.find("span",{"class":"val"}).text
                count+=1
                print(d)
                big_lis.append(d)

        else:
            sub_categories= soup.find_all("li",{"class":"sub-category"})
            for i in sub_categories:
                sub_category_url = i.find("a", href=True)['href']
                r=requests.get(sub_category_url)
                c=r.content
                soup=BeautifulSoup(c,"html.parser")
                product_info= soup.find_all("div",{"class":"col-6 col-md-4 mb-5"})
                count= 1
                for info in product_info:
                    print(count)
                    d={}
                    d["brand"] = info.find("span",{"class":"brand"}).text
                    d["title"] = info.find("span",{"class":"product-name"}).text
                    d["price"] = info.find("span",{"class":"val"}).text
                    count+=1
                    print(d)
                    big_lis.append(d)
    df=pandas.DataFrame(big_lis)
    df.to_csv(str(file_name+".csv"))
