from django.conf.urls import patterns, include, url

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^item/all', 'ppc.views.item.all'),
                       url(r'^item/add', 'ppc.views.item.add'),
                       url(r'^item/update', 'ppc.views.item.update'),
                       url(r'^item/delete', 'ppc.views.item.delete'),
                       url(r'^item/fetch', 'ppc.views.fetch.fetch'),
                       url(r'^tag/all', 'ppc.views.tag.get_tags'),
)