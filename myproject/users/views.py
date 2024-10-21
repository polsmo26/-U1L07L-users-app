from django.shortcuts import render

# Create your views here.

def register(request):
    context = {
        'active_link' : 'register'
    }
    return render(request, 'users/register.html', context)

# def register(request):
#     context = {
#         'active_link': 'register',
#         'register':register
#     }
#     # return render(request, 'register.html', context)
    