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

---

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

## Chapter 3: Django app

#### A big project can be splited into different modules called as Django app.

![URLS_VIEWS](./img/django2.png)

- ### Create the new app inside the project.

```
  python manage.py startapp articles
```

By usintg this command new folder and files will be created representing the articles part of the project.

This folder contains its own views.py(you can create its own urls.py and Template file).

---

## Chapter 4: Model

#### Model is a object used to store data in the database and retrive it.

#### Models python file in the articles app is used for model creations.

- ### MODELS python file.

```python
from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    #
    #

    def __str__(self):
        return self.title

```

To connect and communicate with database we need to migrate the model.

- To migrate the built-in module :

```
  python manage.py migrate
```

- Make a migration file

```
  python manage.py makemigrations
```

- To migrate our own module after creating migration file :

```
  python manage.py migrate
```

After any change in the migration i.e change in model or adding new module we need to migrate to update.

---

## Chapter 5: Django ORM

#### Django ORM is used to communicate or intercte with database.

- Open a new python shell.

```
  python manage.py shell
```

- import Article model to use it.

```
  from articles.modles import Article
```

- To display all objects.

```
  Article.objects.all()
```

- To create a object.

```
  article=Article()
```

- Insert values in a object.

```
  article.title="hello india"
```

- To save the changes of the object in the database.

```
  article.save()
```

- This is a builtin function to display object with one if its value.

```python
   def __str__(self):
       return self.title
```
- We can use modal methods which will help in customizing the data and to other functionality.

```python
   def snippet(self):
       return self.body[:50]...
```
---

## Chapter 6: Django admin

#### We can control the content of a site using **Django admin**

### Create a admin username and password which can be used for admin access and database access.

- To create a admin .

```
  python manage.py createsuperuser
```

- Enter the details .

```
 Username(leave blank for '[yourname]'):
 Email address:
 password:
```

- set our module for admin area (admin python file).

```
from .models import Article
# Register your models here.

admin.site.register(Article)

```

### You can change the details using thr admin interface.

---

## Chapter 7:  Template Tags

### We can send the data to the Html file and present according to the data using the templae tags.

- Sending the data in the response .

```python
  from django.shortcuts import render
  from .models import Article
  # Create your views here.

  def articleHomepage(request):
      # return HttpResponse("homepage")
      articles = Article.objects.all().order_by('date')
      return render(request, 'articles/articleHome.html', {'articles': articles})
```

### Template Tags

   - ####  **{{ }}**:to print the data
   - ####  **{% %}**: to use python code

- Using The template Tags in Html file .

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1.0"
    />
    <title>Articles</title>
    <link rel="stylesheet" href="/static/style.css" />
  </head>
  <body>
    <div class="articles">
      {% for article in articles %}
      <div class="article">
        <h2><a href="#"> {{article.title}} </a></h2>
        <p>{{article.snippet}}..</p>
      </div>
      {% endfor %}
    </div>
  </body>
</html>
```

- In the above we used a model methods in model file for show only a glimps of the paragraph and called that function in the html file

```python
def snippet(self):
        return self.body[:50]

```

---

## Chapter 8: Static files

### We can use the static files like css and images be explicting setting the static file .

- URLS file .

```python
 from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()
```

- Settings python file .

```python
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'assets')
]
```

---
## Chapter 9: URL patterns

### We can create our own url pattern to capture the a url with perticular pattern and we can send that captured url to view file which will customize the output with respective to the url .


-  #### URLS file .
   - Add a re_path will a regular expression. 
```python
 from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

    # path('admin/', admin.site.urls),
    # path(r'about/', views.about),
    # path(r'', views.articleHomepage, ),

    re_path(r'(?P<slug>[\w-]+)/$', views.articleDetailpage)

]

```

- #### VIEWS python file : 

  - In views file add the module for the url pattens with a pattern a function argument .

```python
from django.http import HttpResponse
from django.shortcuts import render

def articleDetailpage(request, slug):
    # return HttpResponse(slug)
    # articles = Article.objects.all().order_by('date')
    # return render(request, 'articles/articleHome.html', {'articles': articles})
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/articleDetail.html', {'article': article})
```

---
## Chapter 9: Named URL

### We can add names to the url and use it in the html page instead of hard coding the url  .

-  ### URLS file .
    - Add third parameter to the path with name as identifiers. 

```python

app_name = 'article'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path(r'about/', views.about),
    path(r'', views.articleHomepage, name="list"),
    re_path(r'(?P<slug>[\w-]+)/$', views.articleDetailpage, name="detail")

]

```

- ### In HTML file : 
  - Use the name of the url in the href of the element .

```html
{% for article in articles %}
	<div class="article">
		<h2>
      <a href="{% url 'article:detail' slug=article.slug%}">
				{{article.title}}
			</a>
		</h2>
		<p>{{article.snippet}}..</p>
	</div>
	{% endfor %}
```

---