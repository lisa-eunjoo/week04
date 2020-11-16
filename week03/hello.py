from pymongo import MongoClient #파이몽고 쓰겠다
client = MongoClient('localhost', 27017) #파이몽고 접근하라
db = client.dbsparta #dbsparta이름의 db에 접근

import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#old_content > table > tbody > tr')

#old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img
#old_content > table > tbody > tr:nth-child(2) > td.point
for tr in trs:
    a_tag = tr.select_one('td.title > div > a')

    if a_tag is not None:
       title = a_tag.text
       rank = tr.select_one('td:nth-child(1) > img')['alt']
       star = tr.select_one('td.point').text
       print(rank + " " + title + " " + star)
       print(rank,title,star)
       doc = {
            'title':title,
            'rank':rank,
            'star':star
       }
       db.movies.insert_one(doc)


