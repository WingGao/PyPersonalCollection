#encoding:utf8
from django.http import HttpResponse
import json, urllib2, re


class FetchItem():
    author = ''
    img = ''

    def to_dict(self):
        return {'author': self.author, 'img': self.img}


def fetch(request):
    url = request.GET['url']
    if (url.index("www.jbook.co.jp")):
        res = get_jbook(url)

    return HttpResponse(json.dumps(res.to_dict()))


def get_jbook(url):
    html = urllib2.urlopen(url).read()
    author = re.findall('<a class="prodauthor".*?>(.*?)</a>', html)[0].split("著")[0]
    author = author.decode('utf-8').replace(u'\u3000', ' ').strip()
    img = re.findall('<img src="(.*?)" class="prodimage"', html)[0]
    f = FetchItem()
    f.author = author
    f.img = img
    return f