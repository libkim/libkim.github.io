import requests
from bs4 import BeautifulSoup
import json
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

tids = [1597, 3380, 6793]
ani_list = []

for tid in tids:
  req = requests.get(f'https://cal.syoboi.jp/tid/{tid}')
  req.encoding = None
  html = req.content
  soup = BeautifulSoup(html, 'html.parser')
  
  ani = {}
  follow_ups = []
  
  follow_ups_path = soup.find_all(
    '#tid_summary > div:nth-child(2) > ul > li'
  )
  for path in follow_ups_path:
    follow_up = {}
    follow_up['title'] = path.find('a').get_text()
    follow_up['ko-title'] = None
    follow_up['premiered'] = path.find('a').decompose().get_text()
    follow_up['bookmark'] = None
    follow_ups.append(follow_up)

  soup.select_one('#main > h1 > span').decompose()
  ani['title'] = soup.select_one(
    '#main > h1'
  ).get_text()
  ani['ko-title'] = None
  ani['premiered'] = soup.select_one(
    '#tidContainer > div.tidTabContentLayout > div.tidSidebar > div > table.section.basic > tbody > tr > td > table > tbody > tr:nth-child(3) > td'
  ).get_text().split('～')[0]
  ani['bookmark'] = None
  ani['follow-ups'] = follow_ups
  ani_list.append(ani)

with open(os.path.join(BASE_DIR, 'ani-list.json'), 'w+',encoding='utf-8') as json_file:
    json.dump(ani_list, json_file, ensure_ascii = False, indent='\t')
