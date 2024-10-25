from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm

# Create your views here.

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        #validate the form
        if form.is_valid():
            form.save()
            return redirect("posts.list")
    else:
        # form = UserCreationForm()
        form = CustomUserCreationForm()
    context = {
        'active_link' : 'register',
        'form':form
    }
    return render(request, 'users/register.html', context)