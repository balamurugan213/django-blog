from django.shortcuts import render ,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
# Create your views here.

def signup_view(request):
    # return HttpResponse("about")
    if request.method == 'POST': 
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            #log the user
            login(request,user)
            return redirect('article:list')
    else:
        form=UserCreationForm()
        return render(request, 'accounts/signup.html',{'form':form})

def login_view(request):
    # return HttpResponse("about")
    if request.method == 'POST': 
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            # form.save()
            #log the user
            user=form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else: 
                return redirect('article:list')
        else:
            return render(request, 'accounts/login.html',{'form':form})
    else:
        form=AuthenticationForm()
        return render(request, 'accounts/login.html',{'form':form})

def logout_view(request):
    # return HttpResponse("about")
    if request.method == 'POST': 
        logout(request)
        return redirect('article:list')
