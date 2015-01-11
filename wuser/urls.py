from django.conf.urls import patterns, include, url

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^login', 'wuser.views.login_view'),
                       url(r'^check', 'wuser.views.check_user'),
)