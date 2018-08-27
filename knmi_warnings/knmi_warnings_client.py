from bubble3 import Bubble
import json
import feedparser

def get_knmi_warnings(warnings_url):
    #wurl='http://projects.knmi.nl/RSSread/rss_KNMIwaarschuwingen.php'
    fd=feedparser.parse(warnings_url)
    print("got knmi feed"+ fd.entries[0]['title'])
    return fd


class BubbleClient(Bubble):
    def __init__(self,cfg={}):
        self.CFG=cfg
        print(cfg)
    def pull(self, amount='all', index=0):
        if amount=='all':
            all_items=True
            self.say('BC: pulling all')
            sl=False
        else:
            all_items=False
            sl=slice(index,index+amount)
            self.say('BC: %d,%d'%(amount,index))
        data=get_knmi_warnings(self.CFG.WARNINGS_RSS_URL)
        self.say(msg='hi',stuff=data)
        ci=0
        dfd=dict(data)
        for d in dfd['entries']:
           if all_items or ci in sl:
                yield d
                ci+=1

