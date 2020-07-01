import requests
import sys
from bs4 import BeautifulSoup
import json


def get_html(url):
  user_agent = ('Chrome/51.0.2704.103')
  r = requests.get(url, headers={'User-Agent': user_agent})
  return r.text


def parse(html):
  soup = BeautifulSoup(html, 'html.parser')
  trendingBox = soup.find_all('article', class_='Box-row', limit=10)
  arrayJSON = []
  for row in trendingBox:
    name_and_author = row.find(
        'h1', class_='h3 lh-condensed').find('a').contents[-2::]
    author = name_and_author[0].string.strip()[:-2]
    name = name_and_author[1].string.strip()
    url = 'https://github.com/' + author + '/' + name
    all_stars = row.find(
        'a', class_='muted-link d-inline-block mr-3').contents[-1].strip().replace(',', '')
    stars_today = row.find(
        'span', class_='d-inline-block float-sm-right').contents[-1].strip()[:-12]
    currentJSON = {
        'name': name,
        'author': author,
        'url': url,
        'stars': all_stars,
        'starsToday': stars_today
    }
    arrayJSON.append(currentJSON)
  f = open('./python/result/result.txt', 'w')
  return f.write(json.dumps(arrayJSON))


print(parse(get_html('https://github.com/trending')))
sys.stdout.flush()
