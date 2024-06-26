from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'home.html')


def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html',{
            'form' : UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # register user 
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                return redirect('tasks')
            except:
                return render(request, "signup.html",{
                    'form' : UserCreationForm,
                    'error' : 'Username already exists'
                })
        return render(request, "signup.html",{
                    'form' : UserCreationForm,
                    'error' : 'Password do not match'
                })


def tasks(request):
    return render(request, 'tasks.html')