from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.core.urlresolvers import reverse
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'login_registration/index.html')

def register(request):
    if request.method == 'POST':
        userObject = User.objects.isValidRegistration(request.POST)
        if 'user' in userObject:
            request.session['id'] = userObject['user'].id 
            request.session['first_name'] = userObject['user'].first_name 
            return redirect(reverse('dashboard'))
        else:
            for error in userObject['errors']:
                messages.warning(request, error)
            return redirect(reverse('index'))
    else:
        return redirect('index')

def login(request):
    if request.method == 'POST':
        userObject = User.objects.isValidLogin(request.POST)
        if 'user' in userObject:
            request.session['id'] = userObject['user'].id 
            request.session['first_name'] = userObject['user'].first_name
            return redirect(reverse('dashboard'))
        else:
            for error in userObject['errors']:
                messages.warning(request, error)
            return redirect(reverse('index'))
