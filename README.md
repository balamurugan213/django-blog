# blog

### Using python Django

![URLS_VIEWS](./img/django0.png)

---
---
## Chapter 1:
- ### Install djanjo in python using pip.
 ```
 pip install Django
 ```
- ### Create the new project.
 ```
   django-admin Startproject blog
 ```
- ### To run project localhost.
 ```
  python manage.py runserver
 ```
 ***
 ## Chapter 2:
 ![URLS_VIEWS](./img/django1.png)
 
- ### URLS python file:
```python
from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('articles/', include('articles.urls')),
    path(r'about/', views.about),
    path(r'', views.homepage)

]
```
- ### VIEWS python file:
```python
from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    # return HttpResponse("about")
    return render(request, 'about.html')


def homepage(request):
    # return HttpResponse("homepage")
    return render(request, 'home.html')
```
The requesr go to urls python file and search for correct url and relevant view function is called which render the html file and send a response.
## Chapter 3:

 #### A big project can be splited into different modules called as Django app.

- ### Create the new app inside the project.
 ```
   python manage.py startapp articles
 ```
By usintg this command new folder and files will be created representing the articles part of the project.
 ***
## Chapter 4:

 #### Model is.

- ### Create the new app inside the project.
 ```
   python manage.py startapp articles
 ```
By usintg this command new folder and files will be created representing the articles part of the project.
 ***

