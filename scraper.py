import requests
from bs4 import BeautifulSoup
import yaml
import os
import sys

ani_list = []
updated_ani_list = []

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KEY_ORDER = ['tid', 'title', 'ko-title', 'premiered', 'bookmark', 'follow-ups']

def create_tid():
  if 'title' in ani:
    url = f"https://cal.syoboi.jp/find?kw={ani['title']}"
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    ani['tid'] = int(soup.find('a', text=f"{ani['title']}")['href'].split('/')[2])

with open(os.path.join(BASE_DIR, 'ani-list.yml')) as file:
  ani_list = yaml.load(file, Loader=yaml.FullLoader)

for ani in ani_list:
  if not 'tid' in ani: # 키가 없거나 값이 없으면
    create_tid()
  elif 'tid' in ani and type(ani['tid']) != 'int': # 값이 있지만 값이 정수가 아니면
    create_tid()
  
  if 'tid' in ani:
    url = f"https://cal.syoboi.jp/tid/{ani['tid']}/summary"
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    
    updated_follow_ups = []
    
    if soup.select_one('#main > h1 > span'):
      soup.select_one('#main > h1 > span').decompose()
      soup.select_one('#main > h1 > a').decompose()
    ani['title'] = soup.select_one('#main > h1').get_text(strip=True) # 무조건 다시 생성
    
    if not 'ko-title' in ani: # 키가 없거나 값이 없으면
      ani['ko-title'] = None
      
    ani['premiered'] = soup.find('table', class_='data').find_all('tr')[2].select_one('td').get_text().split('～')[0] # 무조건 다시 생성
    
    if not 'bookmark' in ani: # 키가 없거나 값이 없으면
      ani['bookmark'] = None

    follow_ups_path = soup.find('ul', class_='tidList').find_all('li')
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

  if not 'follow-ups' in ani:
    del ani['follow-ups']
    
  index_map = {key: index for index, key in enumerate(KEY_ORDER)}
  sorted_ani = dict(sorted(ani.items(), key=lambda k: index_map[k[0]]))
  updated_ani_list.append(sorted_ani)

with open(os.path.join(BASE_DIR, 'ani-list.yml'), 'w', encoding='utf-8') as file:
  yaml.dump(updated_ani_list, file, default_flow_style=False, sort_keys=False, allow_unicode=True)
