#encoding:utf8
from django.http import HttpResponse
import json, urllib2, re


class FetchItem():
    title = ''
    author = ''
    img = ''

    def to_dict(self):
        return {'title': self.title, 'author': self.author, 'img': self.img}


def fetch(request):
    url = request.GET['url']
    if (url.index("www.jbook.co.jp")):
        res = get_jbook(url)

    return HttpResponse(json.dumps(res.to_dict()))


def get_jbook(url):
    opener = urllib2.build_opener()
    opener.addheaders.append(('Cookie', 'SSCTRLJBOOK=R18=yes'))
    html = opener.open(url).read()
    author = re.findall('<a class="prodauthor".*?>(.*?)</a>', html)[0]
    author = author.split("著")[0]
    author = author.decode('utf-8').replace(u'\u3000', ' ').strip()
    img, title = re.findall('<img src="(.*?)" class="prodimage" alt="(.*?)"', html)[0]
    f = FetchItem()
    f.title = title
    f.author = author
    f.img = img
    return f
