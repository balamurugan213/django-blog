from django.shortcuts import render ,redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def signup_view(request):
    # return HttpResponse("about")
    if request.method == 'POST': 
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #log the user
            return redirect('article:list')
    else:
        form=UserCreationForm()
        return render(request, 'accounts/signup.html',{'form':form})


def homepage(request):
    # return HttpResponse("homepage")
    return render(request, 'home.html')
