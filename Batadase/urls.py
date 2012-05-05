from django.conf.urls.defaults import patterns, include, url

from api import urls as api_urls

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^api/', include(api_urls)),
    # Examples:
    # url(r'^$', 'Batadase.views.home', name='home'),
    # url(r'^Batadase/', include('Batadase.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
