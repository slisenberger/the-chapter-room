from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf
from django.template import RequestContext
from django.contrib.auth.models import User #for debugging
@login_required
def index(request):
    return render_to_response('home.html', context_instance = RequestContext(request))

#Logs a user out of the website. 
def logout_view(request):
    logout(request)
    return redirect('/')