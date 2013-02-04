#_*_coding:utf-8 _*_
from django.db import models
from django.contrib.auth.models import User as sUser
from django.utils.translation import ugettext as _

GENDER_CHOICES=(('m',_('Male')),('f',_('Female')))
# Create your models here.
class User(models.Model):
    user=models.ForeignKey(sUser,unique=True)
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    gender=models.CharField(max_length=200,choices=GENDER_CHOICES,default='m')
    #email=models.EmailField()
    birthday=models.DateField(blank=True,auto_now=True)
    #phone=models.CharField(max_length=100,blank=True)
    #avatar=models.FileField(upload_to='avatar', blank=True)


    def __unicode__(self):
        return u'%d — %s %s' % (self.user.id,  self.first_name, self.last_name)

    def get_name(self):
        return self.first_name+' '+self.last_name

    def profile_completed(self):
        return self.first_name!=None and self.first_name!='' \
               and self.last_name!=None and self.last_name!= None






def create_profile(sender,instance,created,**kwargs):
    if created:
        profile=User()
        profile.user=instance
        profile.save()


models.signals.post_save.connect(create_profile,sender=sUser)



