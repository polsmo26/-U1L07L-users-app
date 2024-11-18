from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
# from django.http import HttpResponse

# Create your views here.
def posts_list(request):
    # posts = Post.objects.all()
    posts = Post.objects.all().order_by('date')
    context = {
        'active_link': 'posts_list',
        'posts':posts
    }
    return render(request,'posts/posts_list.html', context)
def post_page(request, slug):
    # return HttpResponse(slug)
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html', {'post':post, 'active_link':'post_page'} )

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        # form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:list')
    else:
        form = PostForm()
    # create = Post.object()
    return render(request, 'posts/create_post.html', {'form':form, 'active_link': 'create_post'})
