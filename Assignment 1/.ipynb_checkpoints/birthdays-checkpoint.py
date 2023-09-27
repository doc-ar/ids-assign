import re
import codecs
import requests
from bs4 import BeautifulSoup

# Opening a file for use
fp = codecs.open('out.txt', mode="w", encoding="utf8")

# Preliminary Setup for Scraping
birth_month = 'september'
birth_day = '2'

url1 = 'https://www.timeanddate.com/on-this-day/' + birth_month + '/' + birth_day
response1 = requests.get(url1)
soup1 = BeautifulSoup(response1.content, 'html.parser')

url2 = 'https://www.britannica.com/on-this-day/' + birth_month + '-' + birth_day
response2 = requests.get(url2)
soup2 = BeautifulSoup(response2.content, 'html.parser')

# Extracting and writing all shared-birthdays
table = soup1.select_one('div.otd-life__block:nth-child(1) > ul.list--big')
fp.write('----------------------- Shared Birthdays -----------------------\n')
for row in table.findAll('h3', attrs={'class':'otd-title'}):
    fp.write('* ' + row.text + '\n')

# Extracting and writing all the historical events
table = soup2.select('div.md-history-event.card.d-flex.mb-20.flex-column.flex-sm-row > div.card-body.font-serif')
fp.write('\n\n----------------------- Historical Events -----------------------\n')
for row in table:
    text = row.text.partition('.')[0] + '.'
    text = re.sub('[\u02bf]*', '', text)
    text = text.lstrip()
    fp.write('* ' + text + '\n')

# Close the txt file
fp.close()