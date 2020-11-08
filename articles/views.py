from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.


def about(request):
    # return HttpResponse("about")
    return render(request, 'about.html')


def articleHomepage(request):
    # return HttpResponse("homepage")
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/articleHome.html', {'articles': articles})

@login_required(login_url="/accounts/login")
def articleCreate(request):
    if request.method == 'POST': 
        form=forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid():
            #   save article
              instance = form.save(commit=False)
              instance.author=request.user
              instance.save()
        #     #log the user
        #     user=form.get_user()
        #     login(request,user)
        #     if 'next' in request.POST:
        #         return redirect(request.POST.get('next'))
        #     else: 
              return redirect('article:list')
        # else:
        #     return render(request, 'accounts/login.html',{'form':form})
    else:
        form = forms.CreateArticle()
        return render(request, 'articles/articleCreate.html',{'form':form})

def articleDetailpage(request, slug):
    # return HttpResponse(slug)
    # articles = Article.objects.all().order_by('date')
    # return render(request, 'articles/articleHome.html', {'articles': articles})
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/articleDetail.html', {'article': article})
