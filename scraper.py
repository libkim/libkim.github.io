import os
import requests
from bs4 import BeautifulSoup
from ruamel.yaml import YAML
from operator import itemgetter

ani_list = []
updated_ani_list = []

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KEY_ORDER = ['tid', 'title', 'ko-title', 'premiered', 'bookmark', 'follow-ups']

def strip_leading_double_space(stream):
  if stream.startswith("  "):
    stream = stream[2:]
  return stream.replace("\n  ", "\n")
  
def create_tid():
  try:
    url = f"https://cal.syoboi.jp/find?kw={ani['title']}"
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    ani['tid'] = int(soup.find('a', string=f"{ani['title']}")['href'].split('/')[2])
  except:
    ani['tid'] = f"{ani['title']}의 tid 검색 결과가 없습니다."

yaml = YAML()
with open(os.path.join(BASE_DIR, 'ani-list.yml')) as file:
  ani_list = yaml.load(file)

for ani in ani_list:
  if not 'tid' in ani or type(ani['tid']) != 'int' and 'title' in ani: # 키가 없거나 키는 있지만 값이 정수가 아니면, 타이틀이 존재하면
    create_tid()
  
  if 'tid' in ani and type(ani['tid']) == 'int':
    url = f"https://cal.syoboi.jp/tid/{ani['tid']}/summary"
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    follow_up_paths = soup.find('ul', class_='tidList').find_all('li')

    if follow_up_paths != [] and follow_up_paths[-1].select_one('a'):
      ani['tid'] = int(follow_up_paths[-1].select_one('a')['href'].split('/')[2])
      url = f"https://cal.syoboi.jp/tid/{ani['tid']}/summary"
      html = requests.get(url)
      soup = BeautifulSoup(html.text, 'html.parser')
      follow_up_paths = soup.find('ul', class_='tidList').find_all('li')

    updated_follow_ups = []
    
    if soup.select_one('#main > h1 > span'):
      soup.select_one('#main > h1 > span').decompose()
      soup.select_one('#main > h1 > a').decompose()
    ani['title'] = soup.select_one('#main > h1').get_text(strip=True) # 무조건 다시 생성
    
    if not 'ko-title' in ani: # 키가 없으면
      ani['ko-title'] = None
      
    premiered = soup.find('th', string='放送期間').parent.select_one('td').get_text().split('～')[0].split('-') # 무조건 다시 생성
    ani['premiered'] = premiered[0] + '-' + premiered[1].zfill(2)

    if not 'bookmark' in ani: # 키가 없으면
      ani['bookmark'] = None

    for path in follow_up_paths:
      updated_follow_up = {}
      if path.select_one('a'):
        updated_follow_up['tid'] = int(path.select_one('a')['href'].split('/')[2])
        updated_follow_up['title'] = path.select_one('a').extract().get_text()
        updated_follow_up['ko-title'] = next((follow_up.get('ko-title') for follow_up in ani.get('follow-ups', []) if follow_up['title'] == updated_follow_up['title']), None)
        updated_follow_up['premiered'] = path.get_text(strip=True).replace('月','').replace('年','-')
        updated_follow_up['bookmark'] = next((follow_up.get('bookmark') for follow_up in ani.get('follow-ups', []) if follow_up['title'] == updated_follow_up['title']), None)
        updated_follow_ups.append(updated_follow_up)
    ani['follow-ups'] = sorted(updated_follow_ups, key=itemgetter('premiered'))
    
  index_map = {key: index for index, key in enumerate(KEY_ORDER)}
  sorted_ani = dict(sorted(ani.items(), key=lambda k: index_map[k[0]]))
  updated_ani_list.append(sorted_ani)

with open('ani-list.yml', 'w') as file:
    yaml.indent(sequence=4, offset=2)
    yaml.dump(ani_list, file, transform=strip_leading_double_space)
