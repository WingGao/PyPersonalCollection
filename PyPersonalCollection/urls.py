from django.conf.urls import patterns, include, url

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'ppc.views.item.show'),
                       url(r'^ppc/', include('ppc.urls')),
                       url(r'^user/', include('wuser.urls')),
                       # machine
                       url(r'^machine/create', 'machine.views.create'),
                       url(r'^machine/get', 'machine.views.get'),
                       url(r'^machine/save', 'machine.views.save'),
                       # Examples:
                       # url(r'^$', 'PyPersonalCollection.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       # url(r'^admin/', include(admin.site.urls)),
)
