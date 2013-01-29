from django.conf.urls import patterns, include, url
from AProject.apps.A21.views import hello
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from AProject import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'AProject.views.home', name='home'),
    # url(r'^AProject/', include('AProject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^hello/', hello),

)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT}))