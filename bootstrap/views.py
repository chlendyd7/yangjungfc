from django.shortcuts import render

# Create your views here.



def index(request):
    return render(request, 'bootstrap/index.html')


def about(request):
    return render(request, 'bootstrap/about.html')


def contact(request):
    return render(request, 'bootstrap/contact.html')


def post(request):
    return render(request, 'bootstrap/post.html')