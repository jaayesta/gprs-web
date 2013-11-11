from django.conf.urls import patterns, include, url
from gprs import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'gprs.views.home', name='home'),
    url(r'^stored/$', 'gprs.views.stored', name='stored'),
    url(r'^export/$', 'gprs.views.export_to_excel', name='export_to_excel'),
    # url(r'^gprs/', include('gprs.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(
            r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}, name='media')
    )
