from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'logoutbroken.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'aaa.views.home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('django_browserid.urls')),
)
