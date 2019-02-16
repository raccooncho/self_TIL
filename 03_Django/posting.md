

1. models.py

   ```python
   from django.db import models
   
   
   
   # Create your models here.
   class Posting(models.Model):
       title = models.CharField(max_length=100)
       content = models.TextField(default='')
       author = models.CharField(default='anonymous', max_length=50)
       created_at = models.DateField(auto_now_add=True)
       
       def __str__(self):
           return f'{self.id}번글 : {self.title}'
   ```

   

2. views.py

   ```python
   from django.shortcuts import render, redirect, resolve_url
   from .models import Posting
   from .forms import PostingForm, PostingModelForm
   
   def index(request):
       return render(request, 'blog/index.html')
   
   # Create your views here.
   
   def create_posting(request):
       if request.method == 'GET':
           form = PostingForm()
           return render(request, 'blog/create_posting.html', { 'form': form })
           # return redirect(resolve_url('blog:index'))
       else:
           form = PostingForm(request.POST)
           if form.is_valid():
               title = form.cleaned_data.get('title')
               content = form.cleaned_data.get('content')
               author = form.cleaned_data.get('author')
               Posting.objects.create(title=title, content=content, author=author)
               return redirect(resolve_url('blog:index'))
           else:
               return redirect(resolve_url('blog:create'))
   ```

   

3. urls.py

   ```python
   from django.urls import path
   from . import views
   
   app_name = 'blog'
   
   urlpatterns = [
       path('', views.index, name='index'),
       path('create_posting/', views.create_posting, name='create')
       
       ]
   ```

   

4. admin.py

   ```python
   from django.contrib import admin
   from .models import Posting
   # Register your models here.
   
   admin.site.register(Posting)
   ```

   

5. base.html

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <meta http-equiv="X-UA-Compatible" content="ie=edge">
       <title>Document</title>
   </head>
   <body>
       {% block body %}
       {% endblock %}
   </body>
   </html>
   ```

   

6. index.html

   ```html
   {% extends 'blog/base.html' %}
   
   {% block body %}
   
   <h1>Index</h1>
   
   {% endblock %}
   ```

   

7. create_posting.html

   ```html
   {% extends 'blog/base.html' %}
   
   {% block body %}
   
   <form action="{% url 'blog:create' %}" method="POST">
       {% csrf_token %}
       {{ form }}
       <input type="submit" name="Submit"/>
   </form>
   
   
   {% endblock %}
   ```

   

### project

1. urls.py

   ```python
   from django.contrib import admin
   from django.urls import path, include
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('blog/', include('blog.urls')),
   ]
   
   ```

   