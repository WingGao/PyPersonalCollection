# coding=utf-8
from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse, HttpResponseBadRequest
from models import *
from mydjango import JSONResponse
from django.contrib.auth.decorators import login_required


@login_required()
def create(request):
    ct = Template('<form method="POST">'
                  'Machine <input name="name"><input type="submit">'
                  '</form>'
                  '<p>{{msg}}</p>')
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        m, info = get_machine(name)
        if m is not None:
            msg = '已存在'
        else:
            m = Machine(name=name)
            m.save()
            msg = '创建成功'
    else:
        msg = ''
    return HttpResponse(ct.render(Context({'msg': msg})))


@login_required()
def get(request):
    obj_list = []
    for m in Machine.objects.all():
        obj = {'name': m.name}
        info = get_last_info(m)
        if info is not None:
            obj['ip'] = info.save_ip
            obj['time'] = info.save_time.strftime('%Y-%m-%d %H:%M:%S')
        obj_list.append(obj)
    return JSONResponse(obj_list)


def save(request):
    name = request.POST.get('name', '')
    m, info = get_machine(name)
    if m is not None:
        info = AliveInfo(machine=m, save_ip=request.META.get("REMOTE_ADDR", ""))
        info.save()
        return HttpResponse(1)
    return HttpResponseBadRequest(0)