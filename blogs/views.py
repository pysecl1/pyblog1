# Create your views here.
from django.contrib.auth.decorators import login_required
from blogs.models import Content
from django.shortcuts import render, redirect, get_object_or_404




@login_required
def wright_posts (request):
    if request.POST:
        post = Content()
        post.post_title = request.POST.get('post_title')
        post.post = request.POST.get('post')
        post.author = request.user.get_profile()
        post.save()
        return redirect('/')
    else:
        from forms import ContentForm
        form = ContentForm()
        return render(request, 'blog/post.html', {'form':form})

def show_posts (request, page=1):
    posts = Content.objects.filter(author=request.user.get_profile()).order_by('-created_at', 'updated_at')

    from django.core.paginator import Paginator

    paginate = Paginator(posts, 10)
    page = request.GET.get('page',1)
    print type (page)
    posts = paginate.page(page)

    return render(request, 'blog/content.html', {'posts':posts})