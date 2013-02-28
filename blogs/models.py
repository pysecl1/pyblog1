import datetime
from django.db import models
from sprofile.models import User
from blog_main.models import Blog
from django.db.models import F
# Create your models here.

class Content (models.Model):
    post = models.TextField()
    post_title = models.CharField(max_length=150)
    author = models.ForeignKey(User)
    blog_id = models.ForeignKey(Blog, default='1')
    c_likes = models.IntegerField(default=0, blank=True)
    created_at  = models.DateTimeField(default=datetime.datetime.now())
    updated_at  = models.DateTimeField(auto_now=True, default=datetime.datetime.now())

    def __unicode__(self):
        return self.post_title

    def plusLike (self, id=None):
        like = Content.objects.get(id=id)
        like.c_likes = F('c_likes') + 1
        like.save()

    def minusLike (self, id=None):
        dislike = Content.objects.get(id=id)
        dislike.c_likes = F('c_likes') - 1
        dislike.save()

class Likes (models.Model):
    user = models.ForeignKey(User)
    like = models.IntegerField(default = 0)
    post = models.ForeignKey(Content, default=1)

    def __unicode__(self):
        return u'%s %s %s' % (self.user, self.like, self.post)
    def isLike (self, id=None, user=None):
        like = Likes.objects.get(post=id, user=user)
        like.like = F('like') + 1
        like.save()

    def unLike (self, id=None, user=None):
        dislike = Likes.objects.get(post=id, user=user)
        dislike.like = F('like') - 1
        dislike.save()


















