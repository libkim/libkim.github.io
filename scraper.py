import requests
from bs4 import BeautifulSoup
import yaml
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

tids = [1597, 3380, 6793, 2003, 6309]
ani_list = []

for tid in tids:
  url = f'https://cal.syoboi.jp/tid/{tid}/summary'
  html = requests.get(url)
  soup = BeautifulSoup(html.text, 'html.parser')

  ani = {}
  follow_ups = []
  
  follow_ups_path = soup.find(
    'ul', class_='tidList'
  ).find_all('li')
  for path in follow_ups_path:
    follow_up = {}
    if path.select_one('a'):
      follow_up['title'] = path.select_one('a').extract().get_text()
      follow_up['ko-title'] = None
      follow_up['premiered'] = path.get_text()
      follow_up['bookmark'] = None
      follow_ups.append(follow_up)

  if soup.select_one('#main > h1 > span'):
    soup.select_one('#main > h1 > span').decompose()
    soup.select_one('#main > h1 > a').decompose()
  ani['title'] = soup.select_one(
    '#main > h1'
  ).get_text(strip=True)
  ani['ko-title'] = None
  ani['premiered'] = soup.find(
    'table', class_='data'
  ).find_all('tr')[2].select_one('td').get_text().split('～')[0]
  ani['bookmark'] = None
  ani['follow-ups'] = follow_ups
  ani_list.append(ani)

with open(os.path.join(BASE_DIR, 'ani-list.yml'), 'w', encoding='utf-8') as file:
  yaml.dump(ani_list, file, default_flow_style=False, sort_keys=False, allow_unicode=True)
