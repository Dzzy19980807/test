import requests
import os


url="http://pvp.qq.com/web201605/js/herolist.json"


for i in range(0,len(requests.get(url).json())):
   
    urlcontent=requests.get(url).json()[i]['ename']

    name=requests.get(url).json()[i]['cname']

    os.mkdir('C:/Users/12819/Desktop/测试/'+name+'/')

    list=requests.get(url).json()[i]['skin_name'].split('|')
    #print(len(list))

    #skinnumber=len(requests.get(url).json()[i]['skin_name'])

    for j in range(1,len(list)+1):
        
        herourl='http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/'+str(urlcontent)+'/'+str(urlcontent)+'-bigskin-'+str(j)+'.jpg'

        if requests.get(herourl).status_code==200:

            herocontent=requests.get(herourl).content

            with open('C:/Users/12819/Desktop/测试/'+name+'/'+list[j-1]+'.jpg','wb') as f:
                f.write(herocontent)
            #print(herocontent)



            #//game.gtimg.cn/images/yxzj/img201606/skin/hero-info/502/502-bigskin-1.jpg
