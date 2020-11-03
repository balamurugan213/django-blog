from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
# Create your views here.


def about(request):
    # return HttpResponse("about")
    return render(request, 'about.html')


def articleHomepage(request):
    # return HttpResponse("homepage")
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/articleHome.html', {'articles': articles})


def articleDetailpage(request, slug):
    # return HttpResponse(slug)
    # articles = Article.objects.all().order_by('date')
    # return render(request, 'articles/articleHome.html', {'articles': articles})
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/articleDetail.html', {'article': article})
