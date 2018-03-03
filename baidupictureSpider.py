import requests
from urllib import parse
import os

leixing = input("请输入想要的图片：")

os.mkdir("C:/"+leixing+"图片/")

page =input("请输入想要爬取的页数：")

keyword=parse.quote(leixing)

for i in range(1,int(page)+1):
    
    print(i)
    #print(keyword)
    url='https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord='+keyword+'&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word='+keyword+'&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn='+str(i*30)+'&rn=30&gsm=1e&1519722251164='
    print(url)

    for j in range(30):
        try:

            text=requests.get(url).json()['data'][j]['thumbURL']
        except:
            print("第"+str(i)+"页第"+str(j+1)+"张图捕获出错！！！")

        print(text)

        picture=requests.get(text).content

        open("C:/"+leixing+"图片/"+text[-20:],"wb").write(picture)
        #print(picture)