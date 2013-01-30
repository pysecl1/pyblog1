from django.db import models
import datetime
# Create your models here.

gender_choices = (('m', 'male'), ('f', 'female'))

class Blogs (models.Model):
    pass
    #user_id = models.ForeignKey()
    title = models.CharField(max_length=50)
    description = models.TextField()
    logo = models.FileField(upload_to='logo', blank=True)
    created_at = models.DateField(blank=True, null=True, default=datetime.date.today())



class Users (models.Model):
    pass
    username = models.CharField(max_length=50)
    gender = models.CharField(max_length=15, choices=gender_choices)
    b_day = models.DateField(blank=True, null=True)


class Posts (models.Model):
    pass
    #blog_id = models.ForeignKey()
    title = models.CharField(max_length=100)
    description = models.TextField()
