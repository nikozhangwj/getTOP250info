import requests
import time
from urllib import request
from lxml import etree

def get_image(image_url,u):
    image_url = image_url.replace("['","").replace("']","")
    Rq = request.Request(image_url)
    Rs = request.urlopen(Rq)
    get_img = Rs.read()
    with open('D:\\pic\\'+'%s.jpg'% u,'wb') as fp:
        fp.write(get_img)
        print('图片%s下载成功'% u)
    return

for a in range(10):
    url = 'https://movie.douban.com/top250?start={}'.format(a*25)
    Headers = {
                'Host':'movie.douban.com',
                'User-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:58.0) Gecko/20100101 Firefox/58.0',
        }
    data= requests.get(url,headers=Headers).content.decode('utf-8')
    s = etree.HTML(data)
    film_title = s.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]/text()')
    image_url = s.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[1]/a/img/@src')
    for i in range(25):
        time.sleep(1)
        name = "{}".format(film_title[i])
        url = "{}".format(image_url[i])
        print(url)
        get_image(url,name)

print('Done!!')
