#encoding:utf8
from django.http import HttpResponse
import json, urllib2, re
from ppc.util import strQ2B


class FetchItem():
    title = ''
    author = ''
    img = None

    def to_dict(self):
        return {'title': self.title.strip(), 'author': self.author.strip(), 'img': self.img}


def fetch(request):
    url = request.GET['url']
    if not url.startswith('http'):
        url = "http://" + url

    if "www.jbook.co.jp" in url:
        res = get_jbook(url)
    # elif "myanimelist.net/anime/" in url:
    #     res = get_mal(url, "anime")
    return HttpResponse(json.dumps(res.to_dict()))


def get_jbook(url):
    opener = urllib2.build_opener()
    opener.addheaders.append(('Cookie', 'SSCTRLJBOOK=R18=yes'))
    html = opener.open(url).read()
    title = re.findall('<span class="prodtitlemain">(.*?)</span>', html)[0]
    author = re.findall('<a class="prodauthor".*?>(.*?)</a>', html)[0]
    author = author.split("著")[0]
    author = author.decode('utf-8').replace(u'\u3000', ' ').strip()
    img = re.findall('<img src="(.*?)" class="prodimage"', html)
    f = FetchItem()
    f.title = strQ2B(title.decode('utf8'))
    f.author = author
    if len(img) > 0:
        f.img = img[0]
    return f
