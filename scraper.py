import requests
from bs4 import BeautifulSoup
import yaml
import os
import sys

ani_list = []
key_order = ['tid', 'title', 'ko-title', 'premiered', 'bookmark', 'follow-ups']

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, 'ani-list.yml')) as file:
  ani_list = yaml.load(file, Loader=yaml.FullLoader)

for ani in ani_list:
  if not 'tid' in ani:
    if 'title' in ani and ani['title'] != None:
      url = f"https://cal.syoboi.jp/find?kw={ani['title']}"
      html = requests.get(url)
      soup = BeautifulSoup(html.text, 'html.parser')
      ani['tid'] = int(soup.find('a', text=f"{ani['title']}")['href'].split('/')[2])
    else:
      ani['tid'] = None
      
  if ani['tid'] != None:
    updated_follow_ups = []
    
    url = f"https://cal.syoboi.jp/tid/{ani['tid']}/summary"
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    
    if soup.select_one('#main > h1 > span'):
      soup.select_one('#main > h1 > span').decompose()
      soup.select_one('#main > h1 > a').decompose()
    ani['title'] = soup.select_one('#main > h1').get_text(strip=True)
    
    if not 'ko-title' in ani:
      ani['ko-title'] = None
      
    ani['premiered'] = soup.find('table', class_='data').find_all('tr')[2].select_one('td').get_text().split('～')[0]
    
    if not 'bookmark' in ani:
      ani['bookmark'] = None

    follow_ups_path = soup.find(
      'ul', class_='tidList'
    ).find_all('li')
    for path in follow_ups_path:
      updated_follow_up = {}
      if path.select_one('a'):
        updated_follow_up['tid'] = int(path.select_one('a')['href'].split('/')[2])
        updated_follow_up['title'] = path.select_one('a').extract().get_text()
        updated_follow_up['ko-title'] = next((follow_up.get('ko-title') for follow_up in ani.get('follow-ups', []) if follow_up['title'] == updated_follow_up['title']), None)
        updated_follow_up['premiered'] = path.get_text()
        updated_follow_up['bookmark'] = next((follow_up.get('bookmark') for follow_up in ani.get('follow-ups', []) if follow_up['title'] == updated_follow_up['title']), None)
        updated_follow_ups.append(updated_follow_up)
    ani['follow-ups'] = updated_follow_ups

    dict(sorted(ani.items(), key=lambda k: key_order.index(k[0])))

with open(os.path.join(BASE_DIR, 'ani-list.yml'), 'w', encoding='utf-8') as file:
  yaml.dump(ani_list, file, default_flow_style=False, sort_keys=False, allow_unicode=True)
