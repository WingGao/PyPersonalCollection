from django.conf.urls import patterns, include, url

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'ppc.views.item.show'),
                       url(r'^item/all', 'ppc.views.item.all'),
                       url(r'^item/add', 'ppc.views.item.add'),
                       url(r'^item/fetch', 'ppc.views.fetch.fetch'),
                       url(r'^tag/all', 'ppc.views.tag.get_tags'),
                       # Examples:
                       # url(r'^$', 'PyPersonalCollection.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       # url(r'^admin/', include(admin.site.urls)),
)
