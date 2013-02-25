# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response, render , redirect
from django.contrib.auth.models import User
from models import Blog
from blogs.models import Content
from django.http import HttpResponseRedirect


from django.views.generic.simple import redirect_to

from models import Blog
from forms import BlogForm



def siteName(request):
    sitename = 'ggg'
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
    #return HttpResponse('<input type="text">')
    #kommented 24.02.2013
    #nach
    blogs = Blog.objects.all()#.order_by ('-created_at')
    #kon
    #user = request.user
    myBlog = Blog().hasBlog(request.user)

    #myBlog.getBlogByUser(user)

##    print 'blogs'
##    print blogs
    return render (request, 'blog/index.html', {'blogs':blogs, 'myBlog':myBlog})
    #return render_to_response("blog/index.html", context_instance=RequestContext(request))

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

        form=BlogForm()
        blog=Blog.objects.filter(user=user);

        return render_to_response('blog/edit.html',{'form':form},context_instance=RequestContext(request));
    else:
        return redirect_to(request,'/');

def create_blog (request):
    if request.POST:
        blog = Blog()
        blog.user = request.user
        blog.title = request.POST.get('blog_title')
        blog.description = request.POST.get('blog_description')
        blog.tags = request.POST.get('blog_tags')
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

