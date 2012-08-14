from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'tcr.views.index', name='home'),
     url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name' : 'login.html'}),
     url(r'^logout/$', 'tcr.views.logout_view'),
     url(r'^guestlist/$', 'guestlists.views.index'),
     url(r'^guestlist/add/$', 'guestlists.views.add'),
    # url(r'^tcr/', include('tcr.foo.urls')),

     #Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

     #Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
