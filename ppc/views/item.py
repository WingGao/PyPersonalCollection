from django.http import HttpResponse, HttpResponseForbidden,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core import serializers
from ..models import *
import json


def show(request):
    return render_to_response('ppc.html')


def all(request):
    items = None
    if 'type' in request.GET:
        type = request.GET['type']
        if type == 'anime':
            items = CItem.objects.filter(type=CItem.ANIME)
        elif type == 'manga':
            items = CItem.objects.filter(type=CItem.MANGA)

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
    return HttpResponse(json.dumps(objs_to_list(items)))


def add(request):
    if request.method == 'POST':
        post = json.loads(request.body)
    elif request.method == 'GET':
        post = request.GET
    item = CItem()
    item.title = post['title'].strip()
    item.type = get_item_type(post['type'])
    item.url = post['url'].strip()
    item.img = post['img'].strip()
    if 'author' in post:
        item.author = post['author'].strip()
    item.score = post.get('score', 0)
    item.save()
    item.tags = get_tags_by_id(post.get('tags', []))
    if 'r' in post and str(post['r']) == '1':
        return HttpResponseRedirect('/g/PyPersonalCollection/webapp/index.html')
    return HttpResponse(item)


def delete(request):
    if 'id' in request.GET:
        item = CItem.objects.get(id=request.GET['id'])
        item.delete()
        return HttpResponse(json.dumps({'err_code': 0}))
    return HttpResponse(json.dumps({'err_code': 1}))


def update(request):
    if request.method == 'POST':
        post = json.loads(request.body)
        item = CItem.objects.get(id=post['id'])
        item.score = post['score']
        item.tags = get_tags_by_id(post.get('tags', []))
        item.save()
        return HttpResponse(json.dumps(item.to_dict()))
    return HttpResponseForbidden()