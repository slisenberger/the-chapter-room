from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from guestlists.models import Guestlist

@login_required
def index(request):
    return render_to_response('guestlists/home.html', context_instance = RequestContext(request))

@login_required
def add(request):
    twelve_range = []
    # random comment to prove my point.
    for num in range(12):
        twelve_range.append(num + 1)
    
    if request.POST:
        return HttpResponse("add button worked")
    return render_to_response('guestlists/add.html', context_instance = RequestContext(request, {"twelve_range" : twelve_range}))
