from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from ..models import *
from ..util import get_full_url
import json
import math
# num of items on one page
ITEM_PAGE_NUM = 50


def show(request):
    return render_to_response('ppc.html')


@login_required()
def all(request):
    items = None
    type = request.GET.get('type')
    for i in CItem.TYPE_CHOICES:
        if i[1] == type:
            items = CItem.objects.filter(type=i[0])

    if items is None:
        items = CItem.objects

    if 'tags' in request.GET:
        tags = request.GET['tags']
        if len(tags) > 0:
            items = items.filter(tags__in=tags.split(','))

    items = items.all()

    if 'sort' in request.GET:
        sort = request.GET['sort']
        if sort == 'newest':
            items = items.order_by('-id')
        elif sort == 'oldest':
            pass
        elif sort == 'highest':
            items = items.order_by('-score')
        elif sort == 'lowest':
            items = items.order_by('score')
        elif sort == 'name':
            items = items.order_by('title')

    try:
        page = int(request.GET['page'])
        if page < 0:
            page = 0
    except:
        page = 0

    return HttpResponse(json.dumps({'items': objs_to_list(items[page * ITEM_PAGE_NUM:(page + 1) * ITEM_PAGE_NUM]),
                                    'pages': math.ceil(items.count() / ITEM_PAGE_NUM)}))


@login_required()
def add(request):
    if request.method == 'POST':
        post = json.loads(request.body)
    elif request.method == 'GET':
        post = request.GET
    item = CItem()
    item.title = post['title'].strip()
    item.type = get_item_type(post['type'])
    item.url = get_full_url(post['url'])
    item.img = post['img'].strip()
    if 'author' in post:
        item.author = post['author'].strip()
    item.score = post.get('score', 0)
    item.save()
    item.tags = get_tags_by_id(post.get('tags', []))
    if 'r' in post and str(post['r']) == '1':
        return HttpResponseRedirect('/webapp/index.html')
    return HttpResponse(item)


@login_required()
def delete(request):
    if 'id' in request.GET:
        item = CItem.objects.get(id=request.GET['id'])
        item.delete()
        return HttpResponse(json.dumps({'err_code': 0}))
    return HttpResponse(json.dumps({'err_code': 1}))


@login_required()
def update(request):
    if request.method == 'POST':
        post = json.loads(request.body)
        item = CItem.objects.get(id=post['id'])
        item.score = post['score']
        item.tags = get_tags_by_id(post.get('tags', []))
        item.save()
        return HttpResponse(json.dumps(item.to_dict()))
    return HttpResponseForbidden()