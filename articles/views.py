from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def about(request):
    # return HttpResponse("about")
    return render(request, 'about.html')


def articleHomepage(request):
    # return HttpResponse("homepage")
    return render(request, 'articles/articleHome.html')
