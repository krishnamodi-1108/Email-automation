import datetime
import time
from time import strftime
import yagmail
import pandas
from news import NewsFeed

email = yagmail.SMTP(user='pythonproject042@gmail.com', password='xxtmrxjpwgppifaj')


def send_email():
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    yesterday = (datetime.datetime.now() - datetime.timedelta(1)).strftime('%Y-%m-%d')
    news_feed = NewsFeed(row['interest'], yesterday, today, 'en')
    email.send(to=f'{row['email']}',
               subject=f'Your {row['interest']} news for today!',
               contents=f'Hi {row['name']},\nSee what\'s on about {row['interest']} today! \n {news_feed.get_data()} .\nKind Regards,\nKrishna')


while True:
    if datetime.datetime.now().hour == 8 and datetime.datetime.now().minute == 30:
        dataframe = pandas.read_excel('people.xlsx')
        for index,row in dataframe.iterrows():
            send_email()
    time.sleep(60)
