from django.http import HttpResponse
from django.shortcuts import render_to_response
from ..models import *
import json,time


def get_tags(request):
    tags = CTag.objects.all()
    return HttpResponse(json.dumps(objs_to_list(tags)))