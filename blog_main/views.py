# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response, render , redirect
from django.contrib.auth.models import User
from models import Blog
from blogs.models import Content
from django.http import HttpResponseRedirect
from django.db import models


from django.views.generic.simple import redirect_to

from models import Blog
from forms import BlogForm



def siteName(request):
    sitename = 'ggg'
##    html = sitename.render(Context({'sitename':sitename}))
##    return render (request, 'blog/base.html', {'sitename':sitename})
    return render (request, 'blog/base.html', {'sitename':sitename})


#def home(request):
#
#    user=request.user
#    anon=user.is_anonymous()
#
#    if(anon):
#        isanon='T';
#    else:
#        isanon='F';
#
#    posts = Content.objects.filter(author=user).order_by('-updated_at')[:10]
#    return render_to_response("blog/index.html",{'posts':posts}, context_instance=RequestContext(request))

def home(request):
    sitename = 'ggg'

    #return HttpResponse('<input type="text">')
    #kommented 24.02.2013
    #nach
    blogs = Blog.objects.all().order_by ('-created_at')
    #kon
    #user = request.user
    myBlog = Blog().hasBlog(request.user)

    #myBlog.getBlogByUser(user)

##    print 'blogs'
##    print blogs
    return render (request, 'blog/index.html', {'blogs':blogs, 'myBlog':myBlog, 'sitename':sitename})
    #return render_to_response("blog/index.html", context_instance=RequestContext(request))

#def wright_post (request):
#    if request.POST:
#        post = Posts()
#        post.title = request.POST.get('post_title')
#        post.description = request.POST.get('post_desc')
#        post.content = request.POST.get('post_content')

def edit_blog(request, id=None):
##    user=request.user;
##    anon=user.is_anonymous()
##    if not anon:
##
##        form=BlogForm()
##        blog=Blog.objects.get(user=user);
##
##        return render_to_response('blog/edit.html',{'form':form},context_instance=RequestContext(request));
##    else:
##        return redirect_to(request,'/');
    blog=Blog.objects.get(id=id);
    if request.method == 'POST':
        pass
    if request.user == blog.user:
        form=BlogForm(instance=blog)
        return render_to_response('blog/edit.html',{'form':form},context_instance=RequestContext(request));


def create_blog (request):
    if request.POST:
        print request.POST
        blog = Blog()
        blog.user = request.user
        blog.title = request.POST.get('title')
        blog.description = request.POST.get('description')
##        blog.tags = request.POST.get('blog_tags')
        blog.save()
        return redirect_to (request, '/')
    else:
        from forms import BlogForm
        form = BlogForm
        return render(request, 'blog/blog.html', {'form':form})

def delBlog (request, id=None):
    if request.POST:
        blog = Blog.objects.get(id=id)
        blog.delete()
        print 'deltanuto'
        #ref = request.META.get('HTTP_REFERER', None)
        if request.META.get('HTTP_REFERER', None):
    	   return HttpResponseRedirect(request.META.get('HTTP_REFERER', None))
    return redirect("/")


def blog_list (request):
    blogs = Blog.objects.all()

##    print 'blogs'
##    print blogs
    return render (request, 'blog/index.html', {'blogs':blogs})

def myBlogs (request):
    myBlog = Blog().hasBlog(request.user)
    return render (request, 'blog/my-blogs.html', {'myBlog':myBlog})

def search (request):

    if request.method == 'GET':
        search_term = request.GET.get('search_term')
        if search_term:
##            search = Blog.objects.filter(title__contains=search_term)
            search_blog = Blog.objects.filter(models.Q(title__contains=search_term) | models.Q(description__contains=search_term))
            search_post = Content.objects.filter(models.Q(post_title__contains=search_term) | models.Q(post__contains=search_term))

            return render (request, 'blog/search.html', {'search_blog':search_blog, 'search_post':search_post,'search_term':search_term})
    return redirect ("/")


