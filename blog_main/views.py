# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response, render , redirect
from django.contrib.auth.models import User

from blogs.models import Content


from django.views.generic.simple import redirect_to
from models import Blog

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
    return render_to_response("blog/index.html", context_instance=RequestContext(request))

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

def create_blog (request):
    if request.POST:
        blog = Blog()
        blog.blog_title = request.POST.get('blog_title')
        blog.blog_description = request.POST.get('blog_description')
        blog.blog_tags = request.POST.get('blog_tags')
        blog.save()
    else:
        from forms import BlogForm
        form = BlogForm
        return render(request, 'blog/blog.html', {'form':form})


def blog_list (request):
    pass

