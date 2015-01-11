from django.conf.urls import patterns, include, url

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'ppc.views.item.show'),
                       url(r'^ppc/', include('ppc.urls')),
                       url(r'^user/', include('wuser.urls')),
                       # Examples:
                       # url(r'^$', 'PyPersonalCollection.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       # url(r'^admin/', include(admin.site.urls)),
)
