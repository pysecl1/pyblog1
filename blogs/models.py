import datetime
from django.db import models
from sprofile.models import User
from blog_main.models import Blog
# Create your models here.

class Content (models.Model):
    post = models.TextField()
    post_title = models.CharField(max_length=150)
    author = models.ForeignKey(User)
    blog_id = models.ForeignKey(Blog, default='1')
    created_at  = models.DateTimeField(auto_now=True, default=datetime.datetime.now())
    updated_at  = models.DateTimeField(auto_now=True, default=datetime.datetime.now())

    def __unicode__(self):
        return self.post_title