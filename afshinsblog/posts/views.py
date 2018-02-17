from django.shortcuts import render

#the root or home page of the blog wich will use template file


def home(request):
    return render(request, 'posts/home.html')
