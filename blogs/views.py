# Create your views here.
from django.contrib.auth.decorators import login_required
from blogs.models import Content
from django.shortcuts import render, redirect, get_object_or_404
from sprofile.models import User
from blog_main.models import Blog




@login_required
def wright_posts (request):

    id = request.GET.get('id')

    if request.POST:
        post = Content()
        post.post_title = request.POST.get('post_title')
        post.post = request.POST.get('post')
        post.author = request.user.get_profile()
        #blog = Blog.objects.filter(id=request.GET.get('id'))
        blog = request.GET.get('id')
        post.blog_id = Blog().getBlogId(blog)
        post.save()
        return redirect('/')
    else:
        from forms import ContentForm
        form = ContentForm()
        return render(request, 'blog/post.html', {'form':form, 'id':id})

def show_posts (request, page=1):


##    print request.GET["name"]
##    print 'POST'

    #print request.user

##    usver = User.objects.annotate().values()
##    print 'usver-print ->'
##    print usver

##    if request.GET.get('name'):
##        if User.objects.filter (first_name=request.GET.get("name")) == request.user:
##            posts = Content.objects.filter(author=request.user.get_profile()).order_by('-created_at', 'updated_at')
##        else:
##            usver = User.objects.filter (first_name=request.GET.get("name"))
####            print 'usver'
####            print usver
##            posts = Content.objects.filter(author=usver).order_by('-created_at', 'updated_at')
##
##    else:
##        posts = Content.objects.filter(author=request.user.get_profile()).order_by('-created_at', 'updated_at')

    if request.GET:
        name = request.GET.get('name')
        blog = request.GET.get('blog')

##          if Content.objects.filter (blog_id=request.GET.get("blog")) == request.user:
##            posts = Content.objects.filter(author=request.user.get_profile()).order_by('-created_at', 'updated_at')
##          else:
            #blog = User.objects.filter (first_name=request.GET.get("blog"))
##            print 'usver'
##            print usver
        posts = Content.objects.filter(blog_id=request.GET.get('blog')).order_by('-created_at', 'updated_at')

    else:
        posts = Content.objects.filter(author=request.GET.get('name')).order_by('-created_at', 'updated_at')

    from django.core.paginator import Paginator, InvalidPage, EmptyPage

    paginator = Paginator(posts, 10)
    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)

##    paginate = Paginator(posts, 10)
##    page = request.GET.get('page',1)
##    print type (page)
##    posts = paginate.page(page)

    return render(request, 'blog/content.html', {'posts':posts,'blog':blog, 'name':name})


def singlePost (request, id=None):
    post = Content.objects.get(id=id)
    return render (request, 'blog/singlepost.html', {'post':post})
















