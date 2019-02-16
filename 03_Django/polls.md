# project(mysite)

1. urls.py

   ```python
   from django.contrib import admin
   from django.urls import path, include
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('polls/', include('polls.urls')),
   ]
   
   ```

   



# app(polls)

1. models.py

   ```python
   import datetime
   from django.db import models
   from django.utils import timezone
   
   # Create your models here.
   class Question(models.Model):
       question_text = models.CharField(max_length=200)
       pub_date = models.DateTimeField('date published') # date published == 가칭, viewer에게 보이는 명칭
       
       def __str__(self):
           return f'{self.id} : {self.question_text}'
       
       def was_published_recently(self):
           return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
       
   class Choice(models.Model):
       question = models.ForeignKey(Question, on_delete=models.CASCADE)  # on_delete -> 질문이 지워지면 해당하는 답변들도 동시에 지워지는 것
       choice_text = models.CharField(max_length=200)
       votes = models.IntegerField(default=0)
       
       def __str__(self):
           return f'{self.id} : {self.choice_text}'
           
           
   # q = Question(question_text='Whats up?')
   # Choice.objects.create(choice_text='hi', question_id=1)
   
   # c = Choice()
   # c.choice_text = 'olleh'
   # c.question = q
   # c.save()
   
   # q.choice_set.create(choice_text='not much')
   
   # c.question # Q1
   # q.choice_set # <quert_set [c1]>
   # q.choice_set.all() # < all choice [] >
   # q.choice_set.count() # 갯수
   
   
   ```

   

2. views.py

   ```python
   from django.shortcuts import render, redirect, resolve_url, get_object_or_404
   from django.http import Http404, HttpResponseRedirect
   from django.urls import reverse
   
   from .models import Question, Choice
   
   # Create your views here.
   def index(request):
       latest_questions = Question.objects.order_by('-pub_date')[:3]
       # all_questions = Question.objects.order_by('-pub_date')
   
       context = { 'latest_questions': latest_questions } #, 'all_questions': all_questions }
       return render(request, 'polls/index.html', context)
   
   def detail(request, question_id):
       # try:
       #     question = Question.objects.get(id=question_id)
       # except Question.DoesNotExist:
       #     raise Http404("Question does not exist")
       question = get_object_or_404(Question, id=question_id)     
       context = { 'question': question }
       return render(request, 'polls/detail.html', context)
   
   def vote(request, question_id):
       if request.method == 'POST':
           question = get_object_or_404(Question, id=question_id)
           try:
               selected_choice = question.choice_set.get(id=request.POST.get('choice'))
           except (KeyError, Choice.DoesNotExist):
               context = { 'question': question, 'error_message': 'Pick right choice' }
               return render(request, 'polls/detail.html', context)
           else:
               selected_choice.votes += 1
               selected_choice.save()
               # POST 데이터를 처리하고 나서는, 언제나 HttpResponseRedirect를 사용한다.
               return HttpResponseRedirect(reverse('polls:question_results', args=(question.id,)))
       else:
           return HttpResponseRedirect(reverse('polls:question_detail', args=(question_id,)))
   
   def results(request, question_id):
       question = get_object_or_404(Question, id=question_id)
       context = { 'question': question }
       return render(request, 'polls/results.html', context)
   
   
   ```

   

3. urls.py

   ```python
   from django.urls import path
   from . import views
   
   app_name = 'polls'
   
   urlpatterns = [
       path('', views.index, name='question_index'),
       path('<int:question_id>/', views.detail, name='question_detail'),
       path('<int:question_id>/vote/', views.vote, name='question_vote'),
       path('<int:question_id>/results/', views.results, name='question_results'),
       ]
   ```

   

4. admin.py

   ```python
   from django.contrib import admin
   from .models import Question, Choice
   # Register your models here.
   
   admin.site.register([Question, Choice])
   ```

   

5. base.html

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <meta http-equiv="X-UA-Compatible" content="ie=edge">
       <title>Polls App</title>
   </head>
   <body>
       {% block body %}
       {% endblock %}
   </body>
   </html>
   ```

   

6. index.html

   ```html
   {% extends 'polls/base.html' %}
   
   {% block body %}
   <h1>This is Polls App</h1>
   {% if latest_questions %}
   <ul>
       {% for question in latest_questions %}
        <li>
            <a href="{% url 'polls:question_detail' question_id=question.id %}">{{ question.question_text }}</a>
        </li>
       {% endfor %}
   </ul>
   {% endif %}
   {% endblock %}
   ```

   

7. detail.html

   ```html
   {% extends 'polls/base.html' %}
   
   {% block body %}
   
   <h1> {{ question.question_text }} </h1>
   
   {% if error_message %}
   <p><strong>{{ error_message }}</strong></p>
   {% endif %}
   
   <form action="{% url 'polls:question_vote' question_id=question.id %}" method="POST">
       {% csrf_token %}
       {% for choice in question.choice_set.all %}
           <div>
               <input type="radio" name="choice" value="{{ choice.id }}" id="choice{{ forloop.counter }}" />
               <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label>
           </div>
       {% endfor %}
       <div>
           <input type="radio" name="choice" value="100" id="choice{{ forloop.counter }}" />
           <label for="choice{{ forloop.counter }}">Fake choice</label>
       </div>
       <input type="submit" value="Submit"/>
       
   </form>
   
   
   
   {% endblock %}
   ```

   

8. results.html

   ```html
   {% extends 'polls/base.html' %}
   
   {% block body %}
   <h1>{{ question.question_text }}</h1>
   
   {% if question.choice_set.all %}
   <ul>
       {% for choice in question.choice_set.all %}
           <li>
               {{ choice.choice_text }} -- {{ choice.votes }} vote{{ choice.votes|pluralize }}
           </li>
       {% endfor %}
   </ul>
   {% endif %}
   <a href="{% url 'polls:question_detail' question_id=question.id %}">Vote again?</a>
   
   {% endblock %}
   ```

   