#_*_coding:utf-8 _*_
from django.db import models
from django.contrib.auth.models import User as sUser
from sprofile.models import User
from django.utils.translation import ugettext as _
import datetime

# Create your models here.

#gender_choices = (('m', 'male'), ('f', 'female'), ('g', 'germofroditto'))

#class Users (models.Model):
#    user = models.ForeignKey(sUser, unique=True)
#    username = models.CharField(max_length=50, unique=True)
#    userlastname = models.CharField(max_length=50, blank=True)
#    gender = models.CharField(max_length=15, choices=gender_choices)
#    b_day = models.DateField(blank=True, null=True)
#    def __unicode__ (self):
#        return self.username



class Blog (models.Model):
    user = models.ForeignKey(sUser)
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    tags = models.CharField(max_length = 255)
    #author = models.ForeignKey(sUser, unique=True)
#    logo = models.FileField(upload_to='logo', blank=True)
    created_at = models.DateField(blank=True, null=True, default=datetime.date.today())
    def __unicode__(self):

        return u'Блог «%s» пользователя %s' % ( self.description, self.user.get_profile())

    def getBlogByUser(self, author):
        return Blog.objects.get(user=author);

    def hasBlog(self, author):
        try:
            myBlogs = Blog.objects.filter(user=author)
            return myBlogs
        except:
            return

    def getBlogId (self, blog):
        return Blog.objects.get(id=blog)

    def lastPosts (self):
        pass





#class Posts (models.Model):
#    blog_id = models.ForeignKey(Blogs)
#    title = models.CharField(max_length=100)
#    description = models.CharField(max_length=255)
#    content = models.TextField()
#    #author = models.ForeignKey(Users.username)
#    #author = models.CharField(max_length=50)
