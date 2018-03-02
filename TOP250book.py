# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import time
import csv

with open('data.csv','w') as csvfile:
    writer = csv.writer(csvfile,dialect='excel')
    for a in range(10):
        url = "https://book.douban.com/top250?start={}".format(a*25)
        headers = {
                'Host':'book.douban.com',
                'User-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:58.0) Gecko/20100101 Firefox/58.0',
        }
        data = requests.get(url).content.decode('utf-8')
        soup = BeautifulSoup(data,"html.parser")
        all_tables = BeautifulSoup(data,"html.parser").find('div',  class_='indent').find_all('table')
        for table in all_tables:
            try:
                time.sleep(0.5)
                title=table.find('div',class_="pl2").find('a').get('title')
                info=table.find('p').get_text()
                rating_num=table.find('span', class_='rating_nums').get_text()
#               print(type(rating_num))
                writer.writerow([title,info,rating_num])
                print("{} {} {}".format(title,info,rating_num))
            except UnicodeEncodeError:
                continue

    csvfile.close()
