# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response, render , redirect
from django.contrib.auth.models import User

from blogs.models import Content


from django.views.generic.simple import redirect_to
from models import Blog

def home(request):

    user=request.user
    anon=user.is_anonymous()

    if(anon):
        isanon='T';
    else:
        isanon='F';

    posts = Content.objects.filter(author=user).order_by('-updated_at')[:10]
    return render_to_response("blog/index.html",{'posts':posts}, context_instance=RequestContext(request))

#def wright_post (request):
#    if request.POST:
#        post = Posts()
#        post.title = request.POST.get('post_title')
#        post.description = request.POST.get('post_desc')
#        post.content = request.POST.get('post_content')

def edit_blog(request):
    user=request.user;
    anon=user.is_anonymous()
    if not anon:
        blog=Blog.getBlogByUser(user);
        print blog;
        return redirect_to(request,'/');
        #return render_to_response('sprof/main.html',{'':user});
    else:
        return redirect_to(request,'/');
