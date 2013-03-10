from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'', include('website.urls', namespace='website')),
)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^%s/(?P<path>.*)$' % settings.MEDIA_URL, 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            }),
    )
