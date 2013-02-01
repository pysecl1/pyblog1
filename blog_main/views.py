# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response, render , redirect
from django.contrib.auth.models import User

def home(request):
    return render_to_response("blog/index.html", context_instance=RequestContext(request))

def profile(request, id=None):
    if id is not None:
        user=User.objects.get(pk=id)
    else:
        user=request.user
    return render(request,'registration/profile.html',{'profile':user})