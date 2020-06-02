import requests
from bs4 import BeautifulSoup

# theatercode 0297 is chengju cgv
url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0297&date=20200605'
html = requests.get(url)

# print(html.txet)
soup = BeautifulSoup(html.text, 'html.parser')
movie_list = soup.select('div.info-movie')
for i in movie_list:
    print(i.select_one('a > strong').text.strip())
