# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response, render , redirect

def home(request):
    return render_to_response("blog/index.html", context_instance=RequestContext(request))