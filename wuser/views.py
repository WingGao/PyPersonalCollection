from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from mydjango import JSONResponse
# Create your views here.
def login_view(request):
    if request.method == 'GET':
        return render_to_response('user-login.html')
    elif request.method == 'POST':
        user = authenticate(username=request.POST.get('name', ''), password=request.POST.get('password', ''))
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(request.GET.get('next', '/user/check'))
        else:
            return HttpResponseRedirect(request.get_full_path())


def check_user(request):
    return JSONResponse({'is_login': request.user.is_authenticated()})