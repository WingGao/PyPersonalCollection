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