import os
import requests
from bs4 import BeautifulSoup
from ruamel.yaml import YAML
from operator import itemgetter

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KEY_ORDER = ['tid', 'title', 'ko-title', 'premiered', 'bookmark', 'follow-ups']

ani_list = []
update_ani_list = []
completed_ani_list = []

def strip_leading_double_space(stream):
  if stream.startswith("  "):
    stream = stream[2:] #스페이싱 앞에 2개씩 제거
  return stream.replace("\n  ", "\n") # ??

def search_tid(title):
  try:
    html = requests.get(f"https://cal.syoboi.jp/find?kw={title}")
    soup = BeautifulSoup(html.text, 'html.parser')
    tid = int(soup.find('a', string=f"{title}")['href'].split('/')[2])
    return tid
  except:
    print(f"{title}의 'tid' 찾을 수 없음.")
    return None

with open(os.path.join(BASE_DIR, 'ani-list.yml')) as file:
  yaml = YAML()
  ani_list = yaml.load(file)

# 반복문 시작
for ani in ani_list:
  if not 'tid' in ani:
    if 'title' in ani:
      ani['tid'] = search_tid(ani['title'])
  else:
    if not isinstance(ani['tid'], int):
      print(f"잘못된 tid '{ani['tid']}' 제거")
      ani['tid'] = None
      
      # 키 순으로 ani 정렬 후 완성 리스트에 추가
      index_map = {key: index for index, key in enumerate(KEY_ORDER)}
      sorted_ani = dict(sorted(ani.items(), key=lambda k: index_map[k[0]]))
      completed_ani_list.append(sorted_ani)
    else:
      html = requests.get(f"https://cal.syoboi.jp/tid/{ani['tid']}/summary")
      soup = BeautifulSoup(html.text, 'html.parser')
      follow_up_paths = soup.find('ul', class_='tidList').find_all('li')
      print(follow_up_paths)

      if follow_up_paths != [] and follow_up_paths[-1].select_one('a'):
        ani['tid'] = int(follow_up_paths[-1].select_one('a')['href'].split('/')[2])
        html = requests.get(f"https://cal.syoboi.jp/tid/{ani['tid']}/summary")
        soup = BeautifulSoup(html.text, 'html.parser')
        follow_up_paths = soup.find('ul', class_='tidList').find_all('li')
        print(follow_up_paths)

      # title 업데이트 / 무조건 다시 생성
      if soup.select_one('#main > h1 > span'):
        soup.select_one('#main > h1 > span').decompose()
        soup.select_one('#main > h1 > a').decompose()
        ani['title'] = soup.select_one('#main > h1').get_text(strip=True)
      else:
        print(f"{ani['tid']}의 'title' 찾을 수 없음.")
        ani['title'] = None
      
      # ko-title 업데이트
      if not 'ko-title' in ani:
        ani['ko-title'] = None
      elif ani['ko-title'] is not None and not isinstance(ani['ko-title'], str):
        ani['ko-title'] = str(ani['ko-title'])

      # premiered 업데이트 / 무조건 다시 생성
      if soup.find('th', string='放送期間').parent.select_one('td'):
        premiered = soup.find('th', string='放送期間').parent.select_one('td').get_text().split('～')[0].split('-')
        ani['premiered'] = premiered[0] + '-' + premiered[1].zfill(2)
      else:
        print(f"{ani['tid']}의 'premiered' 찾을 수 없음.")
        ani['premiered'] = None

      # bookmark 업데이트
      if not 'bookmark' in ani:
        ani['bookmark'] = None

      # follow-ups 업데이트
      updated_follow_ups = []
      for path in follow_up_paths:
        updated_follow_up = {}
        if path.select_one('a'):
          updated_follow_up['tid'] = int(path.select_one('a')['href'].split('/')[2])
          updated_follow_up['title'] = path.select_one('a').extract().get_text()
          updated_follow_up['ko-title'] = next((follow_up.get('ko-title') for follow_up in ani.get('follow-ups', []) if follow_up['title'] == updated_follow_up['title']), None)
          updated_follow_up['premiered'] = path.get_text(strip=True).replace('月','').replace('年','-')
          updated_follow_up['bookmark'] = next((follow_up.get('bookmark') for follow_up in ani.get('follow-ups', []) if follow_up['title'] == updated_follow_up['title']), None)
          updated_follow_ups.append(updated_follow_up)
      ani['follow-ups'] = sorted(updated_follow_ups, key=itemgetter('tid'))
      print('follow-ups 업데이트 종료')

      # 키 순으로 ani 정렬 후 업데이트 리스트에 추가
      index_map = {key: index for index, key in enumerate(KEY_ORDER)}
      sorted_ani = dict(sorted(ani.items(), key=lambda k: index_map[k[0]]))
      update_ani_list.append(sorted_ani)

print('반복문 종료')

# tid 순으로 업데이트 리스트 정렬 후 완성 리스트에 추가
sort(update_ani_list, key=itemgetter('tid'))
completed_ani_list += update_ani_list

print('tid 순으로 업데이트 리스트 정렬 후 완성 리스트에 추가')

with open('ani-list.yml', 'w') as file:
  yaml = YAML()
  yaml.indent(sequence=4, offset=2)
  yaml.dump(completed_ani_list, file, transform=strip_leading_double_space)
