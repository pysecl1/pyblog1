from django.conf.urls import patterns, include, url
from settings import APP_DIR
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'blog_main.views.home', name='home'),
    # url(r'^blog/', include('blog.foo.urls')),
    ##-
    url(r'^$','sprofile.views.main'),
    #url(r'^login/$','sprofile.views.login'),
    #url(r'^logout/$','sprofile.views.logout'),
    #url(r'^registration/$','sprofile.views.registration'),
    #url(r'^profile/$','sprofile.views.profile'),

    #url(r'^users_list/$','sprofile.views.users_list'),

    #url(r'^user_profile/(?P<user_id>\d+)$','sprofile.views.user_profile'),
    ##-

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
