from django.db import models
import datetime
from django.contrib.auth.models import User as sUser
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

#class Blogs (models.Model):
#    user_id = models.ForeignKey(Users)
#    title = models.CharField(max_length=50)
#    description = models.TextField()
#    logo = models.FileField(upload_to='logo', blank=True)
#    created_at = models.DateField(blank=True, null=True, default=datetime.date.today())
#
#
#
#class Posts (models.Model):
#    blog_id = models.ForeignKey(Blogs)
#    title = models.CharField(max_length=100)
#    description = models.CharField(max_length=255)
#    content = models.TextField()
#    #author = models.ForeignKey(Users.username)
#    #author = models.CharField(max_length=50)
