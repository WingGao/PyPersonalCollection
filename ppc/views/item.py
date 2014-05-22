from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core import serializers
from ..models import *
import json


def show(request):
    return render_to_response('ppc.html')


def all(request):
    items = CItem.objects.all()
    return HttpResponse(json.dumps(objs_to_list(items)))


def add(request):
    if request.method == 'POST':
        post = json.loads(request.body)
        item = CItem()
        item.title = post['title']
        item.type = get_item_type(post['type'])
        item.url = post['url']
        item.img = post['img']
        if 'author' in post:
            item.author = post['author']
        item.score = post.get('score', 0)
        item.save()
        item.tags = get_tags_by_id(post.get('tags', []))
    return HttpResponse(item)


def delete(request):
    if 'id' in request.GET:
        item = CItem.objects.get(id=request.GET['id'])
        item.delete()
        return HttpResponse(json.dumps({'err_code': 0}))
    return HttpResponse(json.dumps({'err_code': 1}))


def update(request):
    if 'id' in request.GET:
        get = request.GET
        item = CItem.objects.get(id=get['id'])
        if 'score' in get:
            item.score = get['score']
        item.save()
        return HttpResponse(json.dumps({'err_code': 0, 'item': item.to_dict()}))
    return HttpResponse(json.dumps({'err_code': 1}))