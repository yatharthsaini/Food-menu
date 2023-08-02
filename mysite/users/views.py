from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        # checking the validity of data in form
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f'Welcome {username}, your account is created')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, "users/register.html", {'form': form})

def profilepage(request):
    return render(request, "users/profile.html")
