import datetime
from datetime import timedelta
import time
import requests


def last_days_questions():
    day_to = datetime.datetime.now()
    day_from = day_to - timedelta(days=2)
    url = 'https://api.stackexchange.com//2.3/questions'

    params = {'fromdate': int(time.mktime(day_from.timetuple())),
              'todate': int(time.mktime(day_to.timetuple())),
              'site': 'stackoverflow.com',
              'tagged': 'Python',
              }

    response = requests.get(url=url, params=params)
    if response.status_code == 200:
        print('Cписок вопросов:')
        for item in response.json()['items']:
            print(item['title'])


if __name__ == '__main__':
    last_days_questions()