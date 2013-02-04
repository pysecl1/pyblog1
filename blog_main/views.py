# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response, render , redirect
#from blog_main.models import Posts

def home(request):
    return render_to_response("blog/index.html", context_instance=RequestContext(request))

#def wright_post (request):
#    if request.POST:
#        post = Posts()
#        post.title = request.POST.get('post_title')
#        post.description = request.POST.get('post_desc')
#        post.content = request.POST.get('post_content')