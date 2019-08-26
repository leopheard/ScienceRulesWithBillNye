from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
URL = "https://rss.art19.com/science-rules-with-bill-nye"

@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('all_episodes'),
            'thumbnail': "https://content.production.cdn.art19.com/images/eb/bc/3b/d6/ebbc3bd6-3bf5-491a-8962-2aed7fe5a684/5ee5564adf3b635d8c079a6b08a33e8e807ef4e5b26a45c3eee1691ee85d28062da380cfc6b02840935292138bdee7281d98734578fae5d3fa92425de5c5590a.jpeg"},
   {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('all_episodes1'),
            'thumbnail': "https://content.production.cdn.art19.com/images/eb/bc/3b/d6/ebbc3bd6-3bf5-491a-8962-2aed7fe5a684/5ee5564adf3b635d8c079a6b08a33e8e807ef4e5b26a45c3eee1691ee85d28062da380cfc6b02840935292138bdee7281d98734578fae5d3fa92425de5c5590a.jpeg"},
   ]
    return items

@plugin.route('/all_episodes/')
def all_episodes():
    soup = mainaddon.get_soup(URL)
    playable_podcast = mainaddon.get_playable_podcast(soup)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items

@plugin.route('/all_episodes1/')
def all_episodes1():
    soup = mainaddon.get_soup(URL)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

if __name__ == '__main__':
    plugin.run()
