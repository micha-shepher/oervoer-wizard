from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'oervoer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^wizard/', include('wizard.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
