from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ZED_Annalytics.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^analytics/', 'Analytics.views.index', name="index"),
    url(r'^upload/', 'Analytics.views.save_file', name="upload"),
)
