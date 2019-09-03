import requests
import re
from bs4 import BeautifulSoup

def get_soup(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup)
    return soup
get_soup("https://feeds.feedburner.com/jimhightower")

def get_playable_podcast(soup):
    subjects = []
    for content in soup.find_all('item'):
        try:        
            link = content.find('p class="podcastmediaenclosure"')
            link = link.get('href')
            print "\n\nLink: ", link
            title = content.find('h4 class="itemtitle"')
            title = title.get_text('a')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': “https://hightowerlowdown.org/wp-content/uploads/JimHightower_iTunes.jpg?bcsi-ac-51628d54de0a7217=2C5BEA15000000033lbipXtVkb+58OTtiJhw7dhFeAjRAgAAAwAAAKQ6KgAIBwAAAAAAANMHCwAAAAAA”
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
            link = content.find('p class="podcastmediaenclosure"')
            link = link.get('href')
            print "\n\nLink: ", link
            title = content.find('h4 class="itemtitle"')
            title = title.get_text('a')
        except AttributeError:
            continue
        item = {
                'href': link,
                'title': title,
                'thumbnail': “https://hightowerlowdown.org/wp-content/uploads/JimHightower_iTunes.jpg?bcsi-ac-51628d54de0a7217=2C5BEA15000000033lbipXtVkb+58OTtiJhw7dhFeAjRAgAAAwAAAKQ6KgAIBwAAAAAAANMHCwAAAAAA”,
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
