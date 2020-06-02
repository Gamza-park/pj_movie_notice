import requests
import telegram
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime


def make_url():

    today = str(datetime.today())
    today = today.split(" ")
    today = today[0].replace("-","")
    tomorow = str(int(today) + 1)
    url_link = "http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0297&date="
    return url_link + tomorow



# make a bot
bot = telegram.Bot(token='1298674671:AAGl0WlHMts5MaPX-kkQ7FXlUAD3uo9MuZw')
# theatercode 0297 is chengju cgv
url = make_url()

def movie_function():
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    D_Day1 = soup.select_one('span.round.red')

    if(D_Day1):
        D_Day1  = D_Day1 .find_parent('div', class_='col-times')
        title = D_Day1.select_one('div.info-movie > a > strong').text.strip()
        bot.send_message(chat_id=1015735757, text=title + ' is tomorow open')
        sched.pause()

sched = BlockingScheduler()
sched.add_job(movie_function, 'interval', seconds=30)
sched.start()

