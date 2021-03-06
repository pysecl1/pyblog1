#_*_coding:utf-8 _*_

# Create your views here.
from blogs.models import Content
from models import *
from django.shortcuts import render_to_response, render, redirect
from django.views.generic.simple import redirect_to
from forms import LoginForm
from forms import RegistrationForm
from forms import ProfileForm
from django.template import RequestContext
from django.contrib.auth.views import login as dlogin
from django.contrib.auth.views import logout as dlogout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User as sUser
from django.contrib.auth import views, authenticate
from django.http import HttpResponseRedirect
from sprofile.models import User
from blog_main.models import Blog


def main(request):
    user=request.user
    anon=user.is_anonymous()
    if anon:
        is_anon="Y"
    else:
        is_anon="F"

        #print 'g'+user.get_profile().first_name+'G'

    return render_to_response('sprof/main.html',{'anon':is_anon,'user':user})

def logout(request):
    user=request.user
    anon=user.is_anonymous()
    dlogout(request)
    return redirect_to(request,'/')

#def logout(request):
#    views.logout(request)
#    return redirect('/')

#def login(request):
#
#    if request.POST:
#        '''login'''
#        print request.POST
#        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
#        if user and user.is_active:
#            views.login(request)
#        return redirect('/')
#    else:
#        form=LoginForm()
#    return render(request,"sprof/login.html",{'form':form})

def login(request):
    pass_is_correct=True
    if request.method=='POST':
        #user=User()
        user=authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password'),
        )

        if user and user.is_active:
            dlogin(request)
            if not user.get_profile().profile_completed():

                return redirect_to(request,'/profile/')
            else:
                return redirect_to(request,'/')
        pass_is_correct=False


    form=LoginForm()


    return render_to_response('sprof/login.html',{'form':form,'ok':pass_is_correct}, context_instance=RequestContext(request))


def registration(request):
    pass_is_correct='true'
    user_exist = 'true'
    form=RegistrationForm()

    if request.method=='POST':
        user=sUser()
        user.username=request.POST.get('username')


        if request.POST.get('confirm')==request.POST.get('password'):
            user.set_password(request.POST.get('password'))
            try:
                user.save()
            except:
                user_exist = 'false'
                return render_to_response ('sprof/registration.html',{'form':form,'user_exist':user_exist}, context_instance=RequestContext(request))

            newuser=authenticate(
                username=user.username,
                password=user.password,
            )
            if user and user.is_active:
                dlogin(request)
                print user.is_anonymous()
                return redirect_to(request,'/profile/')
        pass_is_correct='false'




#    if(request.method=='POST'):
#        post=Post()
#        post.title=request.POST.get('title')
#        post.text=request.POST.get('text')
#        post.author=Author.objects.get(id=request.POST.get('author'))
#        post.save()
#        return redirect_to(request,'/posts/')
#

    return render_to_response('sprof/registration.html',{'form':form,'ok':pass_is_correct}, context_instance=RequestContext(request))

def profile(request):
    form=ProfileForm(instance=request.user.get_profile())
    if request.method=='POST':
        form=ProfileForm(instance=request.user.get_profile(), data=request.POST, files=request.FILES)
        if form.is_valid():
            print "VALID"
            form.save()
            return redirect ('/accounts/profile/')


    return render_to_response('sprof/profile.html',{'form':form}, context_instance=RequestContext(request))

def users_list(request):
    user=request.user
    anon=user.is_anonymous()
    if anon:
        res=User.objects.all()
        isanon='T'
    else:
        res=User.objects.exclude(id=user.get_profile().id)
        isanon='F'


    return render_to_response('sprof/userslist.html',{'users':res,'me':request.user,'anon':isanon})


#def user_profile(request,user_id):
#    if user_id!=None:
#        res=User.objects.get(id=user_id);
#    else:
#        user=request.user
#    #print res;
#    user=request.user
#    anon=user.is_anonymous();
#
#    if(anon):
#        isanon='T';
#    else:
#        isanon='F';
#
#    posts = Content.objects.filter(author=user).order_by('-updated_at')[:10]
#    print posts
#    print isanon
#    return render_to_response('sprof/user_profile.html',{'user':res,'me':request.user,'anon':isanon,'posts':posts})

#def user_profile(request,user_id):
#    if user_id!=None:
#        res=User.objects.get(id=user_id)
#    else:
#        user=request.user
#    #print res
#    user=request.user
#    anon=user.is_anonymous()
#
#    if(anon):
#        isanon='T'
#    else:
#        isanon='F'
#
#
#    print isanon
#    return render_to_response('sprof/user_profile.html',{'user':res,'me':request.user,'anon':isanon,})



def user_profile(request, id=None):
    if id:
        user=User.objects.get(pk=id)
        blogs = Blog().hasBlog(user)
    else:
        user=request.user.get_profile()
        blogs = Blog().hasBlog(user)
    return render(request,'sprof/user_profile.html',{'profile':user, 'blogs':blogs})


