import requests
from bs4 import BeautifulSoup
import re

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
songs = soup.select('#body-content > div > div > table > tbody > tr') #원하는 데이터의 가장 가까운 id 찾아서 쓰기
# movies (tr들) 의 반복문을 돌리기
index = 1
pattern = re.compile(r'\s+')

for song in songs:
    # movie 안에 a 가 있으면,
    a_title = song.select_one('td.info > a.title.ellipsis')
    a_name = song.select_one('td.info > a.artist.ellipsis')
    if a_title is not None:
        a_title_text = a_title.text
        a_title_text = re.sub(pattern, '', a_title_text)
        #print(a_name.text)
        print(f'{index}위 {a_title_text} : {a_name.text}')
        index += 1