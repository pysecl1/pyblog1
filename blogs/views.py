# Create your views here.
from django.contrib.auth.decorators import login_required
from blogs.models import Content, Likes
from django.shortcuts import render, redirect, get_object_or_404
from sprofile.models import User
from blog_main.models import Blog
import random
from blogs.forms import ContentForm
from django.http import HttpResponseRedirect
from sprofile.forms import ProfileForm
import datetime
from django.db import models




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
        #return HttpResponseRedirect(request.META.get('HTTP_REFERER', None))
        return HttpResponseRedirect("/content/?blog=%s&name=%s" % (request.GET.get('id'), request.user))
    else:
        from forms import ContentForm
        form = ContentForm()
        return render(request, 'blog/post.html', {'form':form, 'id':id})

@login_required
def editPost (request, id=None):
    post = Content.objects.get(id=id)
    if request.user == post.author.user:
        form=ContentForm(instance = post)
        if request.POST.get('post_title') and request.POST.get('post'):
            form=ContentForm(instance = post, data=request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/content/?blog=%s&name=%s" % (post.blog_id.id, request.user))
            else:
                error = True
                return render (request, 'blog/edit-post.html', {'form':form, 'error':error})

        return render (request, 'blog/edit-post.html', {'form':form})
    return redirect ("/")
##    return HttpResponseRedirect("/content/?blog=%s&name=%s" % (request.POST.get('blog'), request.user))
##    if request.method=='POST':
##        form=ProfileForm(instance=request.user.get_profile(), data=request.POST, files=request.FILES)
##        if form.is_valid():
##            print "VALID"
##            form.save()
##            return redirect_to(request,'/')

@login_required
def delPost (request, id=None):
    if request.POST:
        post = Content.objects.get(id=id)
        post.delete()
        print 'deltanuto'
        #ref = request.META.get('HTTP_REFERER', None)
        return HttpResponseRedirect("/content/?blog=%s&name=%s" % request.POST.get('blog'), request.user.name)
    return redirect("/")

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

        blog_obj = Blog.objects.get(id=blog)

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

    paginator = Paginator(posts, 5)
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

    return render(request, 'blog/content.html', {'posts':posts,'blog':blog, 'name':name, 'blog_obj':blog_obj})


def singlePost (request, id=None):
    post = Content.objects.get(id=id)
    likes = Likes.objects.filter(post = id)
    if not likes:
        likes = False
##    blog = request.POST.get(id)
##    blog_obj = Blog.objects.get(id=blog)
    ref = request.META.get('HTTP_REFERER', None)
    rand=()
    rand = ((random.randint (0, 329)),(random.randint (0, 60)))
    #rand = random.randint (0, 60)
    return render (request, 'blog/singlepost.html', {'post':post, 'rand':rand, 'likes':likes, 'ref':ref})

def likeMe (request, id=None):
    l_u = Likes.objects.filter(models.Q(post = id) & models.Q(user=request.user))
    print 0 in l_u
    if not l_u:
        Content().plusLike(id)
        like = Likes()
        like.user = request.user.get_profile()
        like.like = 0
        like.post = Content.objects.get(id=id)
        like.save()
        Likes().isLike(id, request.user)

    elif Likes.objects.filter(models.Q(user=request.user) & models.Q(like = 0) & models.Q(post=id)):
        Content().plusLike(id)
        Likes().isLike(id, request.user)

    else:
        Content().minusLike(id)
        Likes().unLike(id, request.user)

    ref = request.META.get ('HTTP_REFERER', None)
    return redirect(ref)
















