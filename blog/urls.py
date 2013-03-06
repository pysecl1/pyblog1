from django.conf.urls import patterns, include, url
from settings import APP_DIR
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'blog_main.views.home', name='home'),
    #url(r'^blog/', include('blog.foo.urls')),
    ##-
    url(r'^login/$','sprofile.views.login', name='login'),
    url(r'^logout/$','sprofile.views.logout',name='logout'),
    url(r'^registration/$','sprofile.views.registration', name='registration'),
    url(r'^profile/$','sprofile.views.profile'),
    url(r'^post/','blogs.views.wright_posts'),
    url(r'^like/(?P<id>\d+)$','blogs.views.likeMe', name='like'),
    url(r'^content/','blogs.views.show_posts'),

    url(r'^editblog/','blog_main.views.edit_blog'),

    url(r'^edit-post/(?P<id>\d+)$','blogs.views.editPost', name='editpost'),
    url(r'^myblogs/','blog_main.views.myBlogs', name='myblogs'),
    url(r'^blogs/','blog_main.views.create_blog'),
    url(r'^search/','blog_main.views.search', name='search'),


    #url(r'^users_list/$','sprofile.views.users_list'),

    #url(r'^user_profile/(?P<user_id>\d+)$','sprofile.views.user_profile'),
    ##-
    url(r'^accounts/profile/$','sprofile.views.user_profile', name='sprofile'),
    url(r'^accounts/profile/(?P<id>\d+)$','sprofile.views.user_profile', name='sprofile'),
    url(r'^view_post/(?P<id>\w+)$','blogs.views.singlePost', name='singlepost'),
    url(r'^delpost/(?P<id>\d+)$','blogs.views.delPost', name='delpost'),
    url(r'^delblog/(?P<id>\d+)$','blog_main.views.delBlog', name='delblog'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django.contrib.comments.urls')),
)
#urlpatterns += staticfiles_urlpatterns()
