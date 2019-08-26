import requests
import re
from bs4 import BeautifulSoup

def get_soup(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup))
    return soup
get_soup("https://rss.art19.com/science-rules-with-bill-nye")

def get_playable_podcast(soup):
    subjects = []
    for content in soup.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://is1-ssl.mzstatic.com/image/thumb/Podcasts123/v4/a7/7a/39/a77a3933-b309-c8ad-3482-83189268f684/mza_8140291980230601024.jpeg/600x600bb.jpg",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast(playable_podcast):
    items = []
    for podcast in playable_podcast:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast1(soup):
    subjects = []
    for content in soup.find_all('item', limit=10):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://is1-ssl.mzstatic.com/image/thumb/Podcasts123/v4/a7/7a/39/a77a3933-b309-c8ad-3482-83189268f684/mza_8140291980230601024.jpeg/600x600bb.jpg",
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast1(playable_podcast1):
    items = []
    for podcast in playable_podcast1:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items
