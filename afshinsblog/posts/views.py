from django.shortcuts import render
from .models import Post
# the root or home page of the blog which will use template file


def home(request):
    posts = Post.objects.order_by('pub_date')
    return render(request, 'posts/home.html', {'posts':posts})
